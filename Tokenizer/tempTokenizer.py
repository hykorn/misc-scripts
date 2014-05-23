formulaArray=("iif(L.S1Sig.ConnEst.Att >0, 100* L.S1Sig.ConnEst.Succ/L.S1Sig.ConnEst.Att, 100)",
              "iif( L.Thrp.Time.UL.QCI.1 >0,( L.Thrp.bits.UL.QCI.1 / L.Thrp.Time.UL.QCI.1 ),0)+iif( L.Thrp.Time.UL.QCI.2 >0,( L.Thrp.bits.UL.QCI.2 / L.Thrp.Time.UL.QCI.2 ),0)+iif( L.Thrp.Time.UL.QCI.3 >0,( L.Thrp.bits.UL.QCI.3 / L.Thrp.Time.UL.QCI.3 ),0)+iif( L.Thrp.Time.UL.QCI.4 >0,( L.Thrp.bits.UL.QCI.4 / L.Thrp.Time.UL.QCI.4 ),0)+iif( L.Thrp.Time.UL.QCI.5 >0,( L.Thrp.bits.UL.QCI.5 / L.Thrp.Time.UL.QCI.5 ),0)+iif( L.Thrp.Time.UL.QCI.6 >0,( L.Thrp.bits.UL.QCI.6 / L.Thrp.Time.UL.QCI.6 ),0)+iif( L.Thrp.Time.UL.QCI.7 >0,( L.Thrp.bits.UL.QCI.7 / L.Thrp.Time.UL.QCI.7 ),0)+iif( L.Thrp.Time.UL.QCI.8 >0,( L.Thrp.bits.UL.QCI.8 / L.Thrp.Time.UL.QCI.8 ),0)+iif( L.Thrp.Time.UL.QCI.9 >0,( L.Thrp.bits.UL.QCI.9 / L.Thrp.Time.UL.QCI.9 ),0)",
              "iif(( L.RRC.ConnReq.Att.Emc + L.RRC.ConnReq.Att.HighPri + L.RRC.ConnReq.Att.Mt + L.RRC.ConnReq.Att.MoData )>0,(( L.RRC.ConnReq.Succ.Emc + L.RRC.ConnReq.Succ.HighPri + L.RRC.ConnReq.Succ.Mt + L.RRC.ConnReq.Succ.MoData )/( L.RRC.ConnReq.Att.Emc + L.RRC.ConnReq.Att.HighPri + L.RRC.ConnReq.Att.Mt + L.RRC.ConnReq.Att.MoData ))*100, 100)",
              "( VS.IUB.AttRLAdd + VS.IUB.AttRLSetup +( VS.IUB.AttRLRecfg *2))/1800",
              "iif( ( VS.RRC.AttConnEstab.Sum *( VS.RRC.AttConEst.DCH + VS.RRC.AttConEst.CCH )*( VS.RAB.AttEstabPS.Conv + VS.RAB.AttEstabPS.Str + VS.RAB.AttEstabPS.Int + VS.RAB.AttEstabPS.Bkg ) =0),100,((( VS.RRC.FailConnEstab.Cong / VS.RRC.AttConnEstab.Sum )+( RRC.SuccConnEstab.sum /( VS.RRC.AttConEst.DCH + VS.RRC.AttConEst.CCH ))* VS.RAB.FailEstabPS.Unsup /( VS.RAB.AttEstabPS.Conv + VS.RAB.AttEstabPS.Str + VS.RAB.AttEstabPS.Int + VS.RAB.AttEstabPS.Bkg ))*100) )")




newFormulas = []

attributeArray=('"VS.IUB.AttRLAdd"','"VS.RRC.AttConEst.DCH"')
attributeHash = {'"VS.IUB.AttRLAdd"':'"LH.CELL_AVAILABILITY"',
                 '"VS.RRC.AttConEst.DCH"':'"LH.S1SIG_SR"'}

for i in formulaArray:
    p = ExcelParser()
    p.parse(i)
    #print("NEXT FORMULA\n============\n"+p.extractFunctions())
    newFormulas.append(p.extractFunctions())

#print("=================================\n"+newFormula[3])

#for oneAttribute in attributeArray:
for attributeName, kpiName in attributeHash.iteritems():
    
    # adding '"' is important as partial attribute name would affect precision
    # This is a better solution to find and replace attributes
    for idx, currFormula in enumerate(newFormulas):
        if attributeName in currFormula:
            print attributeName+" found in \n"+ newFormulas[idx]
            newFormulas[idx] = newFormulas[idx].replace(attributeName,kpiName)
            print "Attribute replaced by "+kpiName+"\n"+ newFormulas[idx]