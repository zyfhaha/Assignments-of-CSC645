#ifndef ENVIRONMENT_H
#define ENVIRONMENT_H

#include <cstdio>
#include <cmath>


class Vector2d
{
  public:
    double x, y;
    Vector2d()                   : x(0),y(0) {}
    Vector2d(double x, double y) : x(x),y(y) {}
    Vector2d operator+(const Vector2d &other) const
      { return Vector2d(x+other.x, y+other.y); }
    Vector2d operator-(const Vector2d &other) const
      { return Vector2d(x-other.x, y-other.y); }
    Vector2d operator*(double s) const
      { return Vector2d(x*s, y*s); }
    double abs() const
      { return sqrt(x*x + y*y); }
};



class Polygon
{
  public:
    int n;
    Vector2d *v;

    Polygon(int n) : n(n)
    {
      v = new Vector2d[n];
    }
    ~Polygon()
    {
      delete[] v;
    }
    bool lineCollision(Vector2d p1, Vector2d p2, Vector2d p3, Vector2d p4, double tolerance)
    {
      double tmp = (p1.x-p2.x)*(p3.y-p4.y)-(p1.y-p2.y)*(p3.x-p4.x);
      if(tmp == 0)
        return false;
      Vector2d p(((p1.x*p2.y-p1.y*p2.x)*(p3.x-p4.x)
                 -(p1.x-p2.x)*(p3.x*p4.y-p3.y*p4.x))/tmp,
                 ((p1.x*p2.y-p1.y*p2.x)*(p3.y-p4.y)
                 -(p1.y-p2.y)*(p3.x*p4.y-p3.y*p4.x))/tmp);
      double l1 = ((p3.x-p4.x)*(p.x-p4.x)+(p3.y-p4.y)*(p.y-p4.y))
                  /(pow(p3.x-p4.x,2)+pow(p3.y-p4.y,2));
      double l2 = ((p1.x-p2.x)*(p.x-p2.x)+(p1.y-p2.y)*(p.y-p2.y))
                  /(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2));
      return (l1>=0 && l1<=1 && l2>0+tolerance && l2<1-tolerance);
    }
    bool checkCollision(Vector2d p1, Vector2d p2, double tolerance=0.001)
    {
      for(int i=0; i<n; i++)
        if(lineCollision(p1,p2, v[i],v[(i+1)%n], tolerance))
          return true;
      for(int i=0; i<n; i++)
        if(lineCollision(p1,p2, v[i],v[(i+2)%n], tolerance))
          return true;
      return false;
    }
    bool checkCollision(Vector2d p)
    {
      Vector2d center(0,0);
      for(int i=0; i<n; i++)
        center = center + v[i];
      return !checkCollision(p, center*(1.0/n), -0.001);
    }
};



class Environment
{
  //private:
  public:
    std::vector<Polygon*> obstacles;
    double width, height;
    
    Environment(double width, double height) : width(width),height(height)
    {}
    ~Environment()
    {
      for(unsigned int i=0; i<obstacles.size(); i++)
        delete obstacles[i];
    }
    
    bool checkCollision(Vector2d p)
    {
      for(unsigned int i=0; i<obstacles.size(); i++)
        if(obstacles[i]->checkCollision(p))
          return true;
      return false;
    }
    bool checkCollision(Vector2d p1, Vector2d p2)
    {
      for(unsigned int i=0; i<obstacles.size(); i++)
        if(obstacles[i]->checkCollision(p1,p2))
          return true;
      return false;
    }
    
    void addRandomConvexPolygon()
    {
      int n = rand()%4 + 3;
      bool collision = true;
      Polygon *p = new Polygon(n);
      while(collision)
      {
        //create polygon
        double radius = (double)rand()/RAND_MAX * width/5.0 + width/20.0;
        double x = (double)rand()/RAND_MAX * (width-2.0*radius) + radius;
        double y = (double)rand()/RAND_MAX * (height-2.0*radius) + radius;
        double angle = 0;
        for(int i=0; i<n; i++)
        {
          angle += std::min(M_PI*2.0-angle, 
                            ((double)rand()/RAND_MAX+0.5)*(M_PI*2.0/n));
          p->v[i] = Vector2d(x+cos(angle)*radius,
                             y+sin(angle)*radius);
        }
        //check collisions
        collision = checkCollision(Vector2d(x,y));
        for(int i=0; i<n && !collision; i++)
          if(checkCollision(p->v[i],p->v[(i+1)%n]) || checkCollision(p->v[i]))
            collision = true;
        for(unsigned int i=0; i<obstacles.size() && !collision; i++)
          if(p->checkCollision(obstacles[i]->v[0]))
            collision = true;
      }      
      obstacles.push_back(p);
    }
    
    void saveToFile()
    {
      FILE* f = fopen((char*)"environment.js", "w");
      fprintf(f, "var map =\n\t[\n");
      for(unsigned int i=0; i<obstacles.size(); i++)
      {
        fprintf(f, "\t\t[\n"); 
        for(int j=0; j < obstacles[i]->n; j++)
        {
          fprintf(f, "\t\t\t[%f, %f]", obstacles[i]->v[j].x, obstacles[i]->v[j].y);
          if (j < obstacles[i]->n - 1)
            fprintf(f, ",\n");
          else
            fprintf(f, "\n");
        }
        if (i != obstacles.size() - 1)
          fprintf(f, "\t\t],\n"); 
        else
          fprintf(f, "\t\t]\n\t]\n");
      }
      fclose(f);     

      f = fopen((char*)"environment.txt", "w");
      fprintf(f, "%lu\n", obstacles.size());
      for(unsigned int i=0; i<obstacles.size(); i++)
      {
        fprintf(f, "%d\n", obstacles[i]->n);
        for(int j=0; j < obstacles[i]->n; j++)
          fprintf(f, "%f %f\n", obstacles[i]->v[j].x, obstacles[i]->v[j].y);
      }
      fclose(f);     
    }
};

#endif
