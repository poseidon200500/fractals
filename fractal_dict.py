iterations = 1
speed = 1
f_len = 10
name = '1'
example = {
    '{name}': {
                'angle' : int,
                'axiom' : str,
                'rules' : tuple,
                'start_pos' : tuple,
                'start_angle' : int,
                    },
}

fract_info = {
    'Koh_line': {
                'angle' : 60,
                'axiom' : 'F',
                'rules' : (('F', 'F+F--F+F'),),
                'start_pos' : (0-(3**iterations * f_len/2)/2,0-(3**iterations * f_len/2)/2),
                'start_angle' : 0
                    }, 
    'Koh_star': {
                'angle' : 60,
                'axiom' : 'F--F--F',
                'rules' : (('F','F+F--F+F'),),
                'start_pos' : (0-50*iterations,0+25*iterations),
                'start_angle' : 0
                    },
    'Koh_square': {
                'angle' : 90,
                'axiom' : 'F+F+F',
                'rules' : (('F', 'F-F+F+FFF-F-F+F'),),
                'start_pos' : (0,0-50*iterations),
                'start_angle' : 0,
                    },
    'crystal': {
                'angle' : 90,
                'axiom' : 'F+F+F+F',
                'rules' : (('F', 'FF+F++F+F'),),
                'start_pos' : (0-50*iterations,0-50*iterations),
                'start_angle' : 0,
                    },
    'Dragon_harter': {
                'angle' : 90,
                'axiom' : 'FX',
                'rules' : (('FX', 'FX+FY+'),('FY','-FX-FY')),
                'start_pos' : (0,0),
                'start_angle' : 0,
                    },
    'Serpin_triangle': {
                'angle' : 60,
                'axiom' : 'FXF--FF--FF--FF',
                'rules' : (('F','FF'),('X','--FXF++FXF++FXF--')),
                'start_pos' : (-200,-50),
                'start_angle' : 0,
                    },
    'Tree_heart': {
                'angle' : 60,
                'axiom' : 'F',
                'rules' : (('F','FXF'),('X','[+FX][-FX]'),),
                'start_pos' : (0,0-400),
                'start_angle' : 90,
                    },
    'Curve_32seg': {
                'angle' : 90,
                'axiom' : 'F+F+F+F',
                'rules' : (('F', '-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+'),),
                'start_pos' : (0-100*iterations,0-100*iterations),
                'start_angle' : 0,
                    },
    'Gilbert_curve': {
                'angle' : 90,
                'axiom' : 'A',
                'rules' : (('A','+BF-AFA-FB+'),('B','-AF+BFB+FA-')),
                'start_pos' : (0-iterations*50,0+iterations*50),#x(-f_len*50),y(+f_len*50)
                'start_angle' : -90,
                    },
    'Gosper_curve': {
                'angle' : 60,
                'axiom' : 'FL',
                'rules' : (('F',''),('L','FL-FR--FR+FL++FLFL+FR-'),('R','+FL-FRFR--FR-FL++FL+FR')),
                'start_pos' : (100,200),
                'start_angle' : 0,
                    },
    'Peano_curve': {
                'angle' : 90,
                'axiom' : 'F',
                'rules' : (('F','F-F+F+F+F-F-F-F+F'),),
                'start_pos' : (0,0),
                'start_angle' : 45,
                    },
    'Squares' : {
                'angle' : 45,
                'axiom' : '+FYF++FYF++FYF++FYF+',
                'rules' : (('F','FF',),('X', '+FF++FYF++FYF++FF+'),('Y', '-FF--FXF--FXF--FF-'),),
                'start_pos' : (0,0-250),
                'start_angle' : 0,
                        }
}
