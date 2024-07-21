#first off all install pywhatkit using the command : pip install pywhatkit.
import pywhatkit as pwk
import traceback

#Enter your data
baby = "+97798*******0"
hour = 00
min = 00
message = "Happy Birthday Dear !"
try:
    pwk.sendwhatmsg(baby,message , hour , min)
except Exception as e:
    print(f"An error occurred: {e}")
    print(traceback.format_exc())





