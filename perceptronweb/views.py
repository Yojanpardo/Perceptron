"""Main views"""

from django.views.generic import TemplateView
from perceptronweb.perceptron import Perceptron
import numpy as np
import pandas as pd
import random

class MainView(TemplateView):
    """Main view"""
    template_name = 'perceptronweb/landingpage.html'

class AndView(TemplateView):
    template_name = 'perceptronweb/empty_page.html'

class AndViewFull(TemplateView):
    """And view"""
    #AND
    template_name = 'perceptronweb/andpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            
        X = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])
        d = np.array([0, 0, 0, 1])
        lr = random.random()
        perceptron = Perceptron(input_size=2, lr=lr)
        df = perceptron.fit(X, d)
        b,w1,w2 = perceptron.W
        tablota = df[['iter','X','y','y^','W','el','MAE']].to_html(classes="table table-hover table-dark table-striped table-sm")
        
        try:
            A = int(self.request.GET['A'])
            B = int(self.request.GET['B'])
            if A != None:
                response = True
                context['response']=response
                context['A']=A
                context['B']=B
                context['output']=perceptron.predict(np.array([1,A,B]))
        except Exception as e:
            pass
        
        context['typegate']='AND'
        context['df']=tablota
        context['b']=b
        context['w1']=w1
        context['w2']=w2
        context['lr']=lr
        return context

class NandView(TemplateView):
    template_name = "perceptronweb/empty_nand_page.html"

class NorViewFull(TemplateView):
    template_name = "perceptronweb/nor_page.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        X = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])
        d = np.array([1, 0, 0, 0])
        lr = random.random()
        perceptron = Perceptron(input_size=2, lr=lr)
        df = perceptron.fit(X, d)
        b,w1,w2 = perceptron.W
        tablota = df[['iter','X','y','y^','W','el','MAE']].to_html(classes="table table-hover table-dark table-striped table-sm")
        
        try:
            A = int(self.request.GET['A'])
            B = int(self.request.GET['B'])
            if A != None:
                response = True
                context['response']=response
                context['A']=A
                context['B']=B
                context['output']=perceptron.predict(np.array([1,A,B]))
        except Exception as e:
            pass
        
        context['typegate']='NOR'
        context['df']=tablota
        context['b']=b
        context['w1']=w1
        context['w2']=w2
        context['lr']=lr

        return context
class NandViewFull(TemplateView):
    """Nand view"""
    template_name = 'perceptronweb/nand_page.html'
    #NAND
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        X = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])
        d = np.array([1, 1, 1, 0])
        lr = random.random()
        perceptron = Perceptron(input_size=2, lr=lr)
        df = perceptron.fit(X, d)
        b,w1,w2 = perceptron.W
        tablota = df[['iter','X','y','y^','W','el','MAE']].to_html(classes="table table-hover table-dark table-striped table-sm")
        
        try:
            A = int(self.request.GET['A'])
            B = int(self.request.GET['B'])
            if A != None:
                response = True
                context['response']=response
                context['A']=A
                context['B']=B
                context['output']=perceptron.predict(np.array([1,A,B]))
        except Exception as e:
            pass
        
        context['typegate']='NAND'
        context['df']=tablota
        context['b']=b
        context['w1']=w1
        context['w2']=w2
        context['lr']=lr

        return context
class OrView(TemplateView):
    template_name = "perceptronweb/empty_or_page.html"

class OrViewFull(TemplateView):
    """Or view"""
    template_name = 'perceptronweb/or_page.html'
    #OR
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        X = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])
        d = np.array([0, 1, 1, 1])
        lr = random.random()
        perceptron = Perceptron(input_size=2, lr=lr)
        df = perceptron.fit(X, d)
        b,w1,w2 = perceptron.W
        tablota = df[['iter','X','y','y^','W','el','MAE']].to_html(classes="table table-hover table-dark table-striped table-sm")
        
        print(*perceptron.W)
        
        try:
            A=int(self.request.GET['A'])
            B=int(self.request.GET['B'])
            if A != None:
                response = True
                context['response']=response
                context['A']=A
                context['B']=B
                context['output']=perceptron.predict(np.array([1,A,B]))
        except Exception as e:
            pass
        context['typegate']='OR'
        context['df']=tablota
        context['b']=b
        context['w1']=w1
        context['w2']=w2
        context['lr']=lr
        return context
