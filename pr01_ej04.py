
#(a) Si tu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa está en primero (valor 1) de videojuegos (valor 'videojuegos')
curso_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa==1 and g_comp_2=='Diseño y desarrollo de videojuegos'
#(b) Si tu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa no está en primero de videojuegos. Escribe dos expresiones distintas
curso_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!=1 or g_comp_2!='Diseño y desarrollo de videojuegos'
not(curso_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa==1 and g_comp_2=='Diseño y desarrollo de videojuegos')
#(c) Si tu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa está en enfermeria, medicina o psicologia

g_comp_2=='enfermeria' or g_comp_2=='medicina' or g_comp_2=='psicologia'
#(d) Si tu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa no está en enfermeriaa, medicina ni psicologia. Escribe dos expresiones distintas
not(g_comp_2=='enfermeria' and g_comp_2=='medicina' and g_comp_2=='psicologia')
g_comp_2!='enfermeria' or g_comp_2!='medicina' or g_comp_2!='psicologia'
#(e) Si tu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa y tú estáis en el mismo curso del mismo grado
curso_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa==mi_curso and g_comp_2==mi_grado
#(f) Si tu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa y tú no estáis en el mismo curso del mismo grado.Escribe dos expresiones distintas
curso_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!=mi_curso and g_comp_2==mi_grado
not(curso_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa==mi_curso or g_comp_2!=mi_grado)
#(g) Si tu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa y tú estais en el mismo curso pero no del mismo grado
curso_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa==mi_curso and g_comp_2!=mi_grado
