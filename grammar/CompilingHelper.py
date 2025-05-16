import math

class Helper:
    def __init__(self, compiler):
        self.compiler = compiler

    def getFloatValue(self, variable):
        # jeżeli przekazano liczbę 
        try:
            return round(float(variable), 3)
        except:
            pass

        # Sprawdź w parametrach funkcji
        if self.compiler.isFunction_params:
            value = self.compiler.function_params.get(variable)
            if value is not None:
                try:
                    return round(float(value), 3)
                except:
                    nested_value = self.compiler.variables_values[self.compiler.function_name].get(value)
                    if nested_value is not None:
                        try:
                            return round(float(nested_value), 3)
                        except:
                            pass

        # Sprawdź w zmiennych ogólnych funkcji
        value = self.compiler.variables_values[self.compiler.function_name].get(variable)
        if value is not None:
            try:
                return round(float(value), 3)
            except:
                pass
        return 0.0
    

    def getXYZValue(self, variable):
        axis = self.compiler.function_params.get(variable)
        if axis is None:
            return None
        if axis.find("'") != -1:
            axis = axis.replace("'", "")
            if axis not in ("X", "Y", "Z", "XY", "YZ", "XZ"):
                return None
            return axis
        if self.compiler.variables_values[self.compiler.function_name].get(axis):
            axis = self.compiler.variables_values[self.compiler.function_name].get(axis)
        return axis
    

    def getBoolValue(self, variable):
        value = self.compiler.function_params.get(variable)
        if value in ("true", "false"):
            return value == "true"
        if self.compiler.variables_values[self.compiler.function_name].get(value):
            new_value = self.compiler.variables_values[self.compiler.function_name].get(value)
            if new_value in ("true", "false"):
                return new_value == "true"
        return None
    

    def getStringValue(self, variable):
        value = self.compiler.function_params.get(variable)
        if value.find("'") != -1:
            value = value.replace("'", "")
        else:
            if self.compiler.variables_values[self.compiler.function_name].get(value):
                value = self.compiler.variables_values[self.compiler.function_name].get(value)
        return value
    
    # Metody OGCode
    def forward(self):
        axis = self.getXYZValue("axis")
        length = self.getFloatValue("L")
        if axis is None:
            angle_rad = math.radians(self.compiler.angle)
            x = math.cos(angle_rad)*length 
            y = math.sin(angle_rad)*length
            self.compiler.output.append(f"G1 X{x} Y{y}" if self.compiler.is_pen_up else f"G0 X{x} Y{y} F1000")
        else:
            self.compiler.output.append("G91") # włączenie pozycjonowania względnego
            self.compiler.output.append(f"G1 {axis}{length}" if self.compiler.is_pen_up else f"G0 {axis}{length} F1000")
            self.compiler.output.append("G90") # włączenie pozycjonowania bezwzględnego

    
    def setAngle(self):
        self.compiler.angle = self.getFloatValue("angle")

    
    def setPenTemp(self):
        temp = self.getFloatValue("T")
        self.compiler.output.append(f"M104 S{temp}" if not self.getBoolValue("wait") else f"M109 S{temp}")


    def ground(self):
        surface = self.getXYZValue("surface")
        if surface == "XY":
            self.compiler.output.append("G17")
        elif surface == "XZ":
            self.compiler.output.append("G18")
        elif surface == "YZ":
            self.compiler.output.append("G19")


    def autoLevel(self):
        self.compiler.output.append("G29")
        if self.getBoolValue("save"):
            self.compiler.output.append("M500")


    def turn(self):
        angle = self.getFloatValue("angle")
        self.compiler.angle = (angle + self.compiler.angle)%360


    def move(self):
        x = self.getFloatValue("X")
        y = self.getFloatValue("Y")
        self.compiler.output.append(f"G1 X{x} Y{y}" if self.compiler.is_pen_up else f"G0 X{x} Y{y} F1000")


    def filledCircle(self):
        R = self.getFloatValue("R")
        x0 = self.getFloatValue("X")
        y0 = self.getFloatValue("Y")
        self.compiler.output.append(f"G0 X{x0} Y{y0}")
        self.compiler.output.append(f"M3") # start wrzeciona lub ekstrudera
        self.compiler.output.append("G91") # tryb przyrostowy (łatwiejsze przemieszczanie)
        self.compiler.output.append("M83") # ekstruder w trybie przyrostowym (dla druku 3D)
        for i in range(int(R)):
            self.compiler.output.append("G0 X1 Y0")
            self.compiler.output.append("G2 X1 Y0 I-1 J0")
        self.compiler.output.append("G90") # tryb absolutny
        self.compiler.output.append("M5") # stop wrzeciona
        self.compiler.output.append(f"G0 X{x0} Y{y0}") # kończy na środku koła


    def setTableTemp(self):
        wait = self.getBoolValue("wait")
        temp = self.getFloatValue("T")
        self.compiler.output.append(f"M190 S{temp}" if wait else f"M140 S{temp}")

    
    def unit(self):
        jednostka = self.getStringValue("U")
        if jednostka == "milimeters":
            self.compiler.output.append("G21")
        if jednostka == "inches":
            self.compiler.output.append("G20")

        
    def cooler(self):
        C = self.getBoolValue("C")
        self.compiler.output.append(f"M06" if C else "M107")


    def absolutePositioning(self):
        pos = self.getBoolValue("pos")
        self.compiler.output.append("G90" if pos else "G91")


    def drawLetter(self):
        letter = self.getStringValue("letter")
        L = self.getFloatValue("L")
        W = self.getFloatValue("W")
        x0 = self.getFloatValue("X0")
        y0 = self.getFloatValue("Y0")
        if letter == "M":
            x_left = x0 - W / 2
            x_right = x0 + W / 2
            y_bottom = y0 - L / 2
            y_top = y0 + L / 2

            self.compiler.output.append(f"G0 X{x_left} Y{y_bottom}")    # do lewego dołu (bez rysowania)
            self.compiler.output.append(f"G1 X{x_left} Y{y_top}")       # pion w górę
            self.compiler.output.append(f"G1 X{x0} Y{y_bottom}")        # ukośna do środka
            self.compiler.output.append(f"G1 X{x_right} Y{y_top}")      # ukośna do prawej góry
            self.compiler.output.append(f"G1 X{x_right} Y{y_bottom}")   # pion w dół


    def penDown(self):
        self.compiler.is_pen_up = False
        self.compiler.output.append("G1 Z5 F300") # przestań rysować


    def penUp(self):
        self.compiler.is_pen_up = True
        self.compiler.output.append("G1 Z0 F300") # rysuj


    def cleanNozzle(self):
        self.compiler.output.append("G12")