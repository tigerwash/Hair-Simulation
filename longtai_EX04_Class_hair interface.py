# excise 04 class
# ARCH 591
# Longtai Liao 

import rhinoscriptsyntax as rs
import random as rnd


class hair(object):
    
    def __init__(self, STRSRF, INTU, INTV, CRV):
        self.strsrf = STRSRF
        self.intu = INTU
        self.intv = INTV
        self.ptlist0 = []
        self.rndptlist = []
        self.rndptlist2 = []
        self.rndptlist3 = []
        self.rndvectorlist = []
        self.rndvectorlist2 = []
        self.rndvectorlist3 = []
        
        self.dis = {}
        self.Dis = {}
        self.Crv = CRV
        
    #generate the base points on skin 
    def SurfacePoints0(self):
    
        #ptlist0 = []
        
        Udomain = rs.SurfaceDomain(self.strsrf, 0)
        Vdomain = rs.SurfaceDomain(self.strsrf, 1)
        
        stepU = (Udomain[1] - Udomain[0])/self.intu
        stepV = (Vdomain[1] - Vdomain[0])/self.intv
        
        #PLOT POINTS ON SURFACE)
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                
                #define u and v in terms of step values and i and j
                u = Udomain[0] + stepU * i
                v = Vdomain[0] + stepV * j
                
                point = rs.EvaluateSurface(self.strsrf, u, v)
                self.ptlist0.append(point)
                
        return self.ptlist0
    
    # second layer of points for hair with random affects
    def SurfacePoints(self):
    
        ptMTX = {}
        srfNORM = {}
        rndNORM = {}
        #rndptlist = []
        
        Udomain = rs.SurfaceDomain(self.strsrf, 0)
        Vdomain = rs.SurfaceDomain(self.strsrf, 1)
        
        stepU = (Udomain[1] - Udomain[0])/self.intu
        stepV = (Vdomain[1] - Vdomain[0])/self.intv
        
        #PLOT POINTS ON SURFACE
        count = 0
        self.rndvectorlist = self.rndvector2()
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                
                #define u and v in terms of step values and i and j
                u = Udomain[0] + stepU * i
                v = Vdomain[0] + stepV * j
                
                point = rs.EvaluateSurface(self.strsrf, u, v)
                ptMTX[(i,j)] = point
                
                #find normals at u,v parameters
                srfNORM[(i,j)] = rs.SurfaceNormal(self.strsrf, (u, v))   
    
                
        #CREATE GRID OF OFFSET POINTS DEFINED BY SURFACE NORMALS
        self.Dis = self.distance()
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                srfNORM[(i,j)] = rs.VectorScale(srfNORM[(i,j)], 40000/self.Dis[(i,j)])
                srfNORM[(i,j)] = rs.PointAdd(ptMTX[(i,j)], srfNORM[(i,j)])
                rndNORM[(i,j)] = rs.VectorAdd(srfNORM[(i,j)], self.rndvectorlist[count]*(800/self.Dis[(i,j)]))
                count = count + 1
                #rs.AddPoint(rndNORM[(i,j)])            
                #rs.AddPoint(ptMTX[(i,j)])
                self.rndptlist.append(rndNORM[(i,j)])
        return self.rndptlist
    
                
    # third layer of points for hair with random affects
    def SurfacePoints2(self):
    
        ptMTX = {}
        srfNORM = {}
        rndNORM = {}
        #rndptlist2 = []
        
        Udomain = rs.SurfaceDomain(self.strsrf, 0)
        Vdomain = rs.SurfaceDomain(self.strsrf, 1)
        
        stepU = (Udomain[1] - Udomain[0])/self.intu
        stepV = (Vdomain[1] - Vdomain[0])/self.intv
        
        count = 0
        self.rndvectorlist = self.rndvector() 
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                
                #define u and v in terms of step values and i and j
                u = Udomain[0] + stepU * i
                v = Vdomain[0] + stepV * j
                
                point = rs.EvaluateSurface(self.strsrf, u, v)
                ptMTX[(i,j)] = point
                
                #find normals at u,v parameters
                srfNORM[(i,j)] = rs.SurfaceNormal(self.strsrf, (u, v))   
    
                
        #CREATE GRID OF OFFSET POINTS DEFINED BY SURFACE NORMALS
        #self.Dis = self.distance()
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                srfNORM[(i,j)] = rs.VectorScale(srfNORM[(i,j)], 80000/self.Dis[(i,j)])
                srfNORM[(i,j)] = rs.PointAdd(ptMTX[(i,j)], srfNORM[(i,j)])
                rndNORM[(i,j)] = rs.VectorAdd(srfNORM[(i,j)], self.rndvectorlist[count]*(800/self.Dis[(i,j)]))
                count = count + 1
                #rs.AddPoint(rndNORM[(i,j)])            
                #rs.AddPoint(ptMTX[(i,j)])
                self.rndptlist2.append(rndNORM[(i,j)])
        return self.rndptlist2
    
                
    # forth layer of points for hair with random affects
    def SurfacePoints3(self):
    
        ptMTX = {}
        srfNORM = {}
        rndNORM = {}
        #rndptlist3 = []
        
        Udomain = rs.SurfaceDomain(self.strsrf, 0)
        Vdomain = rs.SurfaceDomain(self.strsrf, 1)
        
        stepU = (Udomain[1] - Udomain[0])/self.intu
        stepV = (Vdomain[1] - Vdomain[0])/self.intv
        
        #PLOT POINTS ON SURFACE
        count = 0
        self.rndvectorlist = self.rndvector() 
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                
                #define u and v in terms of step values and i and j
                u = Udomain[0] + stepU * i
                v = Vdomain[0] + stepV * j
                
                point = rs.EvaluateSurface(self.strsrf, u, v)
                ptMTX[(i,j)] = point
                
                #find normals at u,v parameters
                srfNORM[(i,j)] = rs.SurfaceNormal(self.strsrf, (u, v))   
    
                
        #CREATE GRID OF OFFSET POINTS DEFINED BY SURFACE NORMALS
        self.Dis = self.distance()
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                srfNORM[(i,j)] = rs.VectorScale(srfNORM[(i,j)], 120000/self.Dis[(i,j)])
                srfNORM[(i,j)] = rs.PointAdd(ptMTX[(i,j)], srfNORM[(i,j)])
                rndNORM[(i,j)] = rs.VectorAdd(srfNORM[(i,j)], self.rndvectorlist[count]*(800/self.Dis[(i,j)]))
                count = count + 1
                #rs.AddPoint(rndNORM[(i,j)])            
                #rs.AddPoint(ptMTX[(i,j)])
                self.rndptlist3.append(rndNORM[(i,j)])
                #rs.DeleteObject(rndptlist3)
        return self.rndptlist3
    
    
    #create random vector 1
    def rndvector(self):
        ptList = []
        #rndvectorlist = []
        for i in range(self.intu + 1):
            for j in range(self.intv + 1):
                for k in range(2):
                    x = i * 5+(rnd.random()*50)
                    y = j * 5+(rnd.random()*50)
                    z = k * 20+(rnd.random()*50)
                   
                    point = [x,y,z]
                    opoint = (55,55,55) 
                    #rs.AddPoint(point)
                    rndvector = rs.VectorCreate(opoint, point)
                    self.rndvectorlist.append(rndvector)
        self.rndvectorlist = self.rndvectorlist[0:((self.intu+1) *(self.intv+1))]
        return  self.rndvectorlist 
                    
    #create random vector 2
    def rndvector2(self):
        ptList = []
        #rndvectorlist2 = []
        for i in range(self.intu + 1):
            for j in range(self.intv + 1):
                for k in range(2):
                    x = i * 5+(rnd.random()*50)
                    y = j * 5+(rnd.random()*50)
                    z = k * 20+(rnd.random()*50)
                   
                    point = [x,y,z]
                    opoint = (55,55,55)
                    #rs.AddPoint(point)
                    rndvector2 = rs.VectorCreate(opoint, point)
                    self.rndvectorlist2.append(rndvector2)
        self.rndvectorlist2 = self.rndvectorlist2[0:((self.intu+1) *(self.intv+1))]
        return  self.rndvectorlist2 
        
    def rndvector3(self):
        ptList = []
        #rndvectorlist3 = []
        for i in range(self.intu + 1):
            for j in range(self.intv + 1):
                for k in range(2):
                    x = i * 5+(rnd.random()*50)
                    y = j * 5+(rnd.random()*50)
                    z = k * 20+(rnd.random()*50)
                   
                    point = [x,y,z]
                    opoint = (55,55,55)
                    #rs.AddPoint(point)
                    rndvector3 = rs.VectorCreate(opoint, point)
                    self.rndvectorlist3.append(rndvector3)
        self.rndvectorlist3 = self.rndvectorlist3[0:((self.intu+1) *(self.intv+1))]
        return  self.rndvectorlist3 
    
    #curve interface 
    def distance(self):
        
        Udomain = rs.SurfaceDomain(self.strsrf, 0)
        Vdomain = rs.SurfaceDomain(self.strsrf, 1)
        
        stepU = (Udomain[1] - Udomain[0])/self.intu
        stepV = (Vdomain[1] - Vdomain[0])/self.intv
        
        #PLOT POINTS ON SURFACE)
        for i in range(self.intu+1):
            for j in range(self.intv+1):
                
                #define u and v in terms of step values and i and j
                u = Udomain[0] + stepU * i
                v = Vdomain[0] + stepV * j
                
                point = rs.EvaluateSurface(self.strsrf, u, v)
                
                crvParam = rs.CurveClosestPoint(self.Crv, point)
                crvPoints = rs.EvaluateCurve(self.Crv, crvParam)
                
                if rs.Distance(point, crvPoints) < 400 :
                    self.dis[(i,j)] = rs.Distance(point, crvPoints)
                else :
                    self.dis[(i,j)]= 1300
                
        return self.dis
            
            
def main():
    global intU
    global intV
    strSRF = rs.GetObject('select surface', rs.filter.surface)
    #rs.HideObject(strSRF)
    intU = rs.GetInteger('set U value', 30)
    intV = rs.GetInteger('set V value', 30)
    
    crv = rs.GetObject('select interface curve', rs.filter.curve)
    
    #draw hair
    hairs = hair(strSRF, intU, intV, crv)
    ptlist0 = hairs.SurfacePoints0() 
    rndptlist = hairs.SurfacePoints() 
    rndptlist2 = hairs.SurfacePoints2()
    rndptlist3 = hairs.SurfacePoints3() 

    
    for i in range((intU+1) *(intV+1)):
        points = []
        points.append(ptlist0[i])
        points.append(rndptlist[i])
        points.append(rndptlist2[i])
        points.append(rndptlist3[i])
        rs.AddCurve(points,3)

    
    
main()