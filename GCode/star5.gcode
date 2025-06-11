M201 X2500 Y2500 Z500 E5000
M203 X250 Y250 Z5 E40
M204 P2500 R500 T2500 ; sets acceleration (P, T) and retract acceleration (R)
M205 X10.00 Y10.00 Z0.40 E5.00 ; sets the jerk limits, mm/sec
M220 S100 ;Reset Feedrate
M221 S100 ;Reset Flowrate
M104 S220 ;Set final nozzle temp
M140 S55
M190 S55 ;Set and wait for bed temp to stabilize 
M109 S220
G28
G92 E0 ;Reset Extruder
G1 F1000 
; warstwa 1
G0 Z0.2 F600; move up
G0 X110 Y110 F3000;move to center
M83
G17
G29
M500
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 2
G1 Z0.4
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 3
G1 Z0.6
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 4
G1 Z0.8
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 5
G1 Z1.0
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 6
G1 Z1.2
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 7
G1 Z1.4
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 8
G1 Z1.6
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 9
G1 Z1.8
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 10
G1 Z2.0
G1 X210.0 Y110.0 E5.2632
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X129.1 Y168.78 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X160.0 Y73.67 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X190.9 Y168.78 E5.2633
; kluczowy kąt dla pięcioramiennej gwiazdy
G1 X110.0 Y110.0 E5.2631
; kluczowy kąt dla pięcioramiennej gwiazdy
; warstwa 11
G1 Z2.2
; --- KONIEC ---
G1 E2 F1800 ; retract
G1 Z5 F600
G0 X0 Y0 F3000
M104 S0 ;Turn-off hotend
M140 S0 ;Turn-off bed
M106 S0 ;Turn-off fan 
M84 ;Disable all steppers