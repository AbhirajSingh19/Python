import matplotlib.pyplot as plt 
import time as t 

times = []
mistakes = 0

print("This program would help you in increase your typing speed. Type the word 'Legend' as fast as possible 5 times.")
input("Press return to continue")

while len(times)<5:
    start = t.time()
    word = input("Tpye the word: ")
    end = t.time()
    timeelapsed = end - start

    times.append(timeelapsed)

    if (word != "Legend"):
        mistakes += 1

print("You made " + str(mistakes) + " mistake(s). ")
print("Now lets check the evolution")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)

legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your evolution")
plt.show()