from tokenizer import *

def rpn_to_ast(rpn):
    stack = []
    for n in rpn:
        num_args = (2 if n.token.ttype == "operator-infix" else
                    1 if n.token.ttype.startswith('operator') else
                    n.num_args if n.token.ttype == 'function' else 0)
        n.args = [stack.pop() for _ in range(num_args)][::-1]
        stack.append(n)
    return stack[0]

def walk(ast):
    yield ast
    for arg in getattr(ast, 'args', []):
        for node in walk(arg):
            yield node


rpn = shunting_yard('iif(L.S1Sig.ConnEst.Att >0, 100* L.S1Sig.ConnEst.Succ/L.S1Sig.ConnEst.Att, 100)')
#rpn = shunting_yard('iif( L.Thrp.Time.UL.QCI.1 >0,( L.Thrp.bits.UL.QCI.1 / L.Thrp.Time.UL.QCI.1 ),0)+iif( L.Thrp.Time.UL.QCI.2 >0,( L.Thrp.bits.UL.QCI.2 / L.Thrp.Time.UL.QCI.2 ),0)+iif( L.Thrp.Time.UL.QCI.3 >0,( L.Thrp.bits.UL.QCI.3 / L.Thrp.Time.UL.QCI.3 ),0)+iif( L.Thrp.Time.UL.QCI.4 >0,( L.Thrp.bits.UL.QCI.4 / L.Thrp.Time.UL.QCI.4 ),0)+iif( L.Thrp.Time.UL.QCI.5 >0,( L.Thrp.bits.UL.QCI.5 / L.Thrp.Time.UL.QCI.5 ),0)+iif( L.Thrp.Time.UL.QCI.6 >0,( L.Thrp.bits.UL.QCI.6 / L.Thrp.Time.UL.QCI.6 ),0)+iif( L.Thrp.Time.UL.QCI.7 >0,( L.Thrp.bits.UL.QCI.7 / L.Thrp.Time.UL.QCI.7 ),0)+iif( L.Thrp.Time.UL.QCI.8 >0,( L.Thrp.bits.UL.QCI.8 / L.Thrp.Time.UL.QCI.8 ),0)+iif( L.Thrp.Time.UL.QCI.9 >0,( L.Thrp.bits.UL.QCI.9 / L.Thrp.Time.UL.QCI.9 ),0)')
print(rpn[0])

write_curve = next(node for node in walk(rpn_to_ast(rpn)) if node.token.ttype == 'function' and node.token.tvalue == 'iif')
print(write_curve.args[0].token.tvalue)
print(write_curve.args[1].token.tvalue)
print(write_curve.args[2].token.tvalue)


formulaArray=("iif(L.S1Sig.ConnEst.Att >0, 100* L.S1Sig.ConnEst.Succ/L.S1Sig.ConnEst.Att, 100)",
              "iif( L.Thrp.Time.UL.QCI.1 >0,( L.Thrp.bits.UL.QCI.1 / L.Thrp.Time.UL.QCI.1 ),0)+iif( L.Thrp.Time.UL.QCI.2 >0,( L.Thrp.bits.UL.QCI.2 / L.Thrp.Time.UL.QCI.2 ),0)+iif( L.Thrp.Time.UL.QCI.3 >0,( L.Thrp.bits.UL.QCI.3 / L.Thrp.Time.UL.QCI.3 ),0)+iif( L.Thrp.Time.UL.QCI.4 >0,( L.Thrp.bits.UL.QCI.4 / L.Thrp.Time.UL.QCI.4 ),0)+iif( L.Thrp.Time.UL.QCI.5 >0,( L.Thrp.bits.UL.QCI.5 / L.Thrp.Time.UL.QCI.5 ),0)+iif( L.Thrp.Time.UL.QCI.6 >0,( L.Thrp.bits.UL.QCI.6 / L.Thrp.Time.UL.QCI.6 ),0)+iif( L.Thrp.Time.UL.QCI.7 >0,( L.Thrp.bits.UL.QCI.7 / L.Thrp.Time.UL.QCI.7 ),0)+iif( L.Thrp.Time.UL.QCI.8 >0,( L.Thrp.bits.UL.QCI.8 / L.Thrp.Time.UL.QCI.8 ),0)+iif( L.Thrp.Time.UL.QCI.9 >0,( L.Thrp.bits.UL.QCI.9 / L.Thrp.Time.UL.QCI.9 ),0)",
              "iif(( L.RRC.ConnReq.Att.Emc + L.RRC.ConnReq.Att.HighPri + L.RRC.ConnReq.Att.Mt + L.RRC.ConnReq.Att.MoData )>0,(( L.RRC.ConnReq.Succ.Emc + L.RRC.ConnReq.Succ.HighPri + L.RRC.ConnReq.Succ.Mt + L.RRC.ConnReq.Succ.MoData )/( L.RRC.ConnReq.Att.Emc + L.RRC.ConnReq.Att.HighPri + L.RRC.ConnReq.Att.Mt + L.RRC.ConnReq.Att.MoData ))*100, 100)",
              "( VS.IUB.AttRLAdd + VS.IUB.AttRLSetup +( VS.IUB.AttRLRecfg *2))/1800",
              "iif( ( VS.RRC.AttConnEstab.Sum *( VS.RRC.AttConEst.DCH + VS.RRC.AttConEst.CCH )*( VS.RAB.AttEstabPS.Conv + VS.RAB.AttEstabPS.Str + VS.RAB.AttEstabPS.Int + VS.RAB.AttEstabPS.Bkg ) =0),100,((( VS.RRC.FailConnEstab.Cong / VS.RRC.AttConnEstab.Sum )+( RRC.SuccConnEstab.sum /( VS.RRC.AttConEst.DCH + VS.RRC.AttConEst.CCH ))* VS.RAB.FailEstabPS.Unsup /( VS.RAB.AttEstabPS.Conv + VS.RAB.AttEstabPS.Str + VS.RAB.AttEstabPS.Int + VS.RAB.AttEstabPS.Bkg ))*100) )")

for i in formulaArray:
    p = ExcelParser()
    p.parse(i)
    print("NEXT FORMULA\n============\n"+p.extractFunctions())

#write_curve = next(node for node in walk(rpn_to_ast(rpn)) if node.token.ttype == 'function' and node.token.tvalue == 'iif')
#print(write_curve.args[0].token.tvalue)
#print(write_curve.args[1].token.tvalue)
#print(write_curve.args[2].token.tvalue)

#for n in rpn:3
#    print("<"+n.token.ttype+" "+n.token.tsubtype+">"+" "+n.token.tvalue)
