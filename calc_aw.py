"""
        A = V / R
	P = V * A
"""
from pynomo.nomographer import *
import pyx
import math

V_params_1={
	'u_min':3.0,
	'u_max':8.5,
	'function':lambda u:math.log10(u),
	'tick_levels':4,
	'tick_text_levels':2,
	'scale_type':'manual line',
	'manual_axis_data': {
		3.0: '3.0V',
		3.2: '3.2V',
		3.7: '3.7V',
		5.0: '5.0V',
		7.4: '7.4V',
		8.5: '8.5V'
		},
	'axis_color':pyx.color.cmyk.Plum,
	'text_color':pyx.color.cmyk.Plum,
}

R_params={
	'u_min':0.1,
	'u_max':1.3,
	'function':lambda u:-math.log10(u),
	'title':r'$\Large\Omega$',
	'tick_levels':0,
	'tick_text_levels':0,
	'extra_params': [
		{
			'u_min': 0.1,
			'u_max': 0.2,
			'tick_levels': 3,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Red,
		},
		{
			'u_min': 0.2,
			'u_max': 1.0,
			'tick_levels': 4,
			'tick_text_levels': 2,
			'axis_color': pyx.color.cmyk.Green,
		},
		{
			'u_min': 1.0,
			'u_max': 1.3,
			'tick_levels': 2,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Blue,
		},
	],
	'text_color':pyx.color.cmyk.Blue,
}

A_params_1={
	'u_min':3.0,
	'u_max':25.0,
	'function':lambda u:-math.log10(u),
	'title':r'$Amps$',
	'tick_levels':0,
	'tick_text_levels':0,
	'tag':'calc_amps',
	'extra_params': [
		{
			'u_min': 3.0,
			'u_max': 10.0,
			'tick_levels': 3,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Blue,
		},
		{
			'u_min': 10.0,
			'u_max': 20.0,
			'tick_levels': 3,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Green,
		},
		{
			'u_min': 20.0,
			'u_max': 25.0,
			'tick_levels': 2,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Red,
		},
	],
}


A_params_2={
	'u_min':3.0,
	'u_max':25.0,
	'function':lambda u:math.log10(u),
	'tick_side':'left',
	'tick_levels':0,
	'tick_text_levels':0,
	'tag':'calc_amps',
	'extra_params': [
		{
			'u_min': 3.0,
			'u_max': 10.0,
			'tick_levels': 3,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Blue,
		},
		{
			'u_min': 10.0,
			'u_max': 20.0,
			'tick_levels': 3,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Green,
		},
		{
			'u_min': 20.0,
			'u_max': 25.0,
			'tick_levels': 2,
			'tick_text_levels': 1,
			'axis_color': pyx.color.cmyk.Red,
		},
	],
}

V_params_2={
	'u_min':3.0,
	'u_max':8.5,
	'function':lambda u:math.log10(u),
	'tick_side':'left',
	'tick_levels':4,
	'tick_text_levels':2,
	'scale_type':'manual line',
	'manual_axis_data': {
		3.0: '3.0V',
		3.2: '3.2V',
		3.7: '3.7V',
		5.0: '5.0V',
		7.4: '7.4V',
		8.5: '8.5V'
		},
	'axis_color':pyx.color.cmyk.Plum,
	'text_color':pyx.color.cmyk.Plum,
}

P_params={
	'u_min':1.0,
	'u_max':100.0,
	'function':lambda u:-math.log10(u),
	'title':r'$Watts$',
	'tick_side':'left',
	'tick_levels':3,
	'tick_text_levels':1,
	'axis_color':pyx.color.cmyk.Sepia,
	'text_color':pyx.color.cmyk.Sepia,
}

# A = V / R
block_1_params={
	'block_type':'type_1',
	'f1_params':V_params_1,
	'f2_params':R_params,
	'f3_params':A_params_1,
	'mirror_x':True,
	'isopleth_values':[
		[3.0,1.0,'x'],
		[3.7,0.5,'x'],
		[3.7,0.3,'x'],
		[3.7,0.15,'x'],
		[7.4,0.6,'x'],
	],
}

# P = V * A
block_2_params={
	'block_type':'type_1',
	'f1_params':A_params_2,
	'f2_params':V_params_2,
	'f3_params':P_params,
	'mirror_x':False,
	'isopleth_values':[
		['y',3.0,'y'],
		['y',3.7,'y'],
		['y',3.7,'y'],
		['y',3.7,'y'],
		['y',7.4,'y'],
	],
}


main_params={
	'filename':'aw.pdf',
	'paper_height':27.7,
	'paper_width':18.0,
	'block_params':[block_1_params, block_2_params],
	'transformations':[('scale paper',)],
	'title_str':r'$A=V\div R \; \& \;  P=V\times A$',
	'isopleth_params':
		[{'color':'Orange',
		'linewidth':'thin',
		'linestyle':'dashdotted',}],
}
Nomographer(main_params)


