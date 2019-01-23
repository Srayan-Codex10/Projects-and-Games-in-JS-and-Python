def rgb_hex():
  invalid_msg = "Please Enter values in RGB format..."
  red = int(raw_input("Enter Red value, R: "))
  if red < 0 or red > 255:
    print invalid_msg
    return
  green = int(raw_input("Enter Green value, G: "))
  if green < 0 or green > 255:
    print invalid_msg
    return
  blue = int(raw_input("Enter Blue value, B: "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  print("RGB: (%d,%d,%d)" %(red,green,blue))
  val = (red << 16) + (green << 8) + blue
  print("Hex Value: #%s " % ((hex(val)[2:]).upper()))
#rgb_hex()

def hex_rgb():
  hex_val = raw_input("Enter Hex Value: ")
  hex_val = hex_val.upper()
  print("HEX: {}".format(hex_val))
  if len(hex_val) != 6:
    print("Invalid Input!!")
    return
  else:
    hex_val = int(hex_val,16)
  two_hex_digits = 2 ** 8 
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print("RGB : (%d,%d,%d) " %(red,green,blue))
  
#hex_rgb()
  
def convert():
  while(True):
    option = str(raw_input("Enter 1 to convert RGB -> HEX \nEnter 2 to convert HEX -> RGB\nEnter X to Exit...\n -> "))
    if option == '1':
      rgb_hex()
    elif option == '2':
      hex_rgb()
    elif option == 'X' or 'x':
      print("Exiting...")
      break
    else:
      print("ERROR!!")
      
convert()