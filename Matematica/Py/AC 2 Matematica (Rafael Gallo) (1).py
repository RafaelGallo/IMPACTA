#!/usr/bin/env python
# coding: utf-8

# # AC 2 Matematica

# Nome: Rafael Henrique Gallo
# RA: *******

# # Exercício - 1

# In[ ]:


import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# A) F(X) y = x

# In[ ]:


def f(x): return x
x = np.linspace(-6,6)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# B) y = -x

# In[ ]:


def f(x): return -x
x = np.linspace(-6,6)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -x")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# C) y = x+2

# In[ ]:


def f(x): return x+2
x = np.linspace(-10,10)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x + 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# D) y = -x+2

# In[ ]:


def f(x): return -x+2
x = np.linspace(-5, 5)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= - x + 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# E) y = x - 2

# In[ ]:


def f(x): return x-2
x = np.linspace(-10, 10)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x - 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# F) y = 2x

# In[ ]:


def f(x): return 2*x
x = np.linspace(-6,6)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x2x")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# G) y = -2x

# In[ ]:


def f(x): return -2*x
x = np.linspace(-6,6)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -2x")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# H) y = 2x+2

# In[ ]:


def f(x): return 2*x+2
x = np.linspace(-6,6)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= 2x + 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.grid()
plt.show()


# i) y = -2x - 2

# In[ ]:


def f(x): return -2*x - 2
x = np.linspace(-5,5)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -2x - 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.grid()
plt.show()


# J) y = -3x + 2

# In[ ]:


def f(x): return -3*x + 2
x = np.linspace(-5,5)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -3x + 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.grid()
plt.show()


# k) y = x2

# In[ ]:


def f(x): return x**2
x = np.linspace(-6,6)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# l) y= -x2

# In[ ]:


def f(x): return -x**2
x = np.linspace(-9,9)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -x2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# m) y = -x2

# In[ ]:


def f(x): return -x*2
x = np.linspace(-8, 8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -x2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# n) y = x2 + 1

# In[ ]:


def f(x): return x*2 + 1
x = np.linspace(-8,8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x*2 + 1")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# o) x2 - 1

# In[ ]:


def f(x): return x**2-1
x = np.linspace(-9, 9)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x*2 - 1")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# p) y = x2 + 3x - 2

# In[ ]:


def f(x): return x**2 + 3*x - 2
x = np.linspace(-8,8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x2 + 3x - 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# q) y = -x2 - 3x - 2

# In[ ]:


def f(x): return -x**2 - 3* - 2
x = np.linspace(-2.5,2.5)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -x2 - 3x - 2")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# r) y = x3

# In[ ]:


def f(x): return x**3
x = np.linspace(-8,8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= x3")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# s) y = -x3

# In[ ]:


def f(x): return -x**3
x = np.linspace(-8,8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= -x3")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# t) y = ln(x)

# In[ ]:


def f(x): return np.log(x)
x = np.linspace(-8, 8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("F(x) ln x")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# u) y = cosec(x)

# In[ ]:


def f(x): return np.cosh(x)
x = np.linspace(-8,8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= cosec(x)")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# v) y = ex

# In[ ]:


def f(x): return np.e**x
x = np.linspace(-8,8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= ex")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# w) y = sec(x)

# In[ ]:


def f(x): return np.sinh(x)
x = np.linspace(-2.5,2.5)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= sec(x)")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# x) y = tg(x)

# In[ ]:


def f(x): return np.tan(x)
x = np.linspace(-8, 8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= tg(x)")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# y) y = cotg (x)

# In[ ]:


def f(x): return np.tanh(x)
x = np.linspace(-2.5,2.5)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= cotg(x)")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# z) y = e-x

# In[ ]:


def f(x): return np.e**-x
x = np.linspace(-8, 8)

plt.plot(x, f(x))
plt.plot(x, f(x), color="black")

plt.title("Função F(X)= e-x")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()


# In[ ]:




