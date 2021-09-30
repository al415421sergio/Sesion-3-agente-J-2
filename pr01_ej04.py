print('recientemente sergio es un pedassso de pelotudo')

#(a) Si tu compañero está en primero (valor 1) de videojuegos (valor 'videojuegos')
curso_compañero==1 and grado_compañero=='Diseño y desarrollo de videojuegos'
#(b) Si tu compañero no está en primero de videojuegos. Escribe dos expresiones distintas
curso_compañero!=1 or grado_compañero!='Diseño y desarrollo de videojuegos'
not(curso_compañero==1 and grado_compañero=='Diseño y desarrollo de videojuegos')
#(c) Si tu compañero está en enfermeria, medicina o psicologia
grado_compañero=='enfermeria' or grado_compañero=='medicina' or grado_compañero=='psicologia'
#(d) Si tu compañero no está en enfermeriaa, medicina ni psicologia. Escribe dos expresiones distintas
not(grado_compañero=='enfermeria' and grado_compañero=='medicina' and grado_compañero=='psicologia')
grado_compañero!='enfermeria' or grado_compañero!='medicina' or grado_compañero!='psicologia'
#(e) Si tu compañero y tú estáis en el mismo curso del mismo grado
curso_compañero==mi_curso and grado_compañero==mi_grado
#(f) Si tu compañero y tú no estáis en el mismo curso del mismo grado.Escribe dos expresiones distintas
curso_compañero!=mi_curso and grado_compañero==mi_grado
not(curso_compañero==mi_curso or grado_compañero!=mi_grado)
#(g) Si tu compañero y tú estais en el mismo curso pero no del mismo grado
curso_compañero==mi_curso and grado_compañero!=mi_grado
