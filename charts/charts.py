import matplotlib.pyplot as plt

def generatePieChart():
    labels = ['A', 'B', 'C']
    values = [200, 500, 800]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    plt.savefig('pie.png')
    plt.close()