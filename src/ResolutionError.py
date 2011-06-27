__author__ = 'Rishi'

class ResolutionError(Exception):

    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return "Invalid Screen Resolution: %dx%d" % self.width,self.height
    def __repr__(self):
        return "Invalid Screen Resolution: %dx%d" % self.width,self.height
    def __unicode__(self):
        return "Invalid Screen Resolution: %dx%d" % self.width,self.height