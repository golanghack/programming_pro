#! /usr/bin/env python3 

"""<--TRANGULUM AWAI CIRCULUM-->"""


def triangle_circumcenter(trinagle: list):
    """find trangle circumcenter"""
    
    x = complex(trinagle[0][0], trinagle[0][1])
    y = complex(trinagle[1][0], trinagle[1][1])
    z = complex(trinagle[2][0], trinagle[2][1])
    
    complex_width = z - x 
    complex_width /= y - x 
    
    c = (x - y) * (complex_width - abs(complex_width) ** 2) / 2j /complex_width.imag - x
    radius = abs(c + x)
    return ((f'point x -> {0 - c.real:.2f} point y -> {0 - c.imag:.2f}'), f'radius -> {radius:.2f}')
  
if __name__ == '__main__':
    print(triangle_circumcenter([[0.8, 0.2], [0.5, 0.2], [0.6, 0.7]]))