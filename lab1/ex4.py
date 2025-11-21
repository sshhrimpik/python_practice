import numpy as np
import matplotlib.pyplot as plt

com, ir, sir, afg = map(int, input('введите данные (4 значения)').split())
with plt.xkcd():
    plt.pie([com, ir, sir, afg], labels = ('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
    plt.title('Где ведутся самые ожесточенные бои')
plt.show()