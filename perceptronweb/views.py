"""Main views"""

from django.views.generic import TemplateView
from perceptronweb.perceptron import Perceptron
import numpy as np
import pandas as pd


class MainView(TemplateView):
    """Main view"""
    template_name = 'perceptronweb/landingpage.html'

class AndView(TemplateView):
    """And view"""
    #AND
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    d = np.array([0, 0, 0, 1])
     
    perceptron = Perceptron(input_size=2, lr=0.5)
    df = perceptron.fit(X, d)
    b,w1,w2 = perceptron.W
    tablota = df[['iter','X','y','y^','W','el', 'MAE']].to_html(classes="table table-hover table-dark table-striped table-sm")

    extra_context = {'typegate':'AND', 'df':tablota, 'b':b, 'w1':w1,'w2':w2}
    template_name = 'perceptronweb/andpage.html'

class NandView(TemplateView):
    """Nand view"""
    template_name = 'perceptronweb/landingpage.html'
    #NAND
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    d = np.array([1, 1, 1, 0])
     
    perceptron = Perceptron(input_size=2, lr=1)
    perceptron.fit(X, d)
    print(*perceptron.W)


class OrView(TemplateView):
    """Or view"""
    template_name = 'perceptronweb/landingpage.html'
    #OR
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    d = np.array([0, 1, 1, 1])
     
    perceptron = Perceptron(input_size=2, lr=1)
    perceptron.fit(X, d)
    print(*perceptron.W)
