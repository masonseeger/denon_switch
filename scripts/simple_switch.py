#!C:/Users/Mason/Miniconda3/python.exe
#Need the above to point to wherever the python.exe file is on your computer
import denonavr #super important package, makes an object that controls denon receiver
import sys

def main():
    print("Content-Type: text/html\n\n") # just used as convention
    try:
        if sys.argv[2] == 'one': #The station given is one
            d = denonavr.DenonAVR('10.61.20.10') #set IP for station one
            d.input_func = sys.argv[1] # change the input of station one
            print("Input on station " + sys.argv[2]+ " successfully changed to " + sys.argv[1])
        else:
            d = denonavr.DenonAVR('10.61.22.58')#set IP for station two
            d.input_func = sys.argv[1]
            print("Input on station " + sys.argv[2]+ " successfully changed to " + sys.argv[1])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
