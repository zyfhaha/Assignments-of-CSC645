#include <cstdio>
#include <cstdlib>
#include <vector>
#include <ctime>

#include "Environment.h"

int main(int argc, char* argv[])
{   
  srand(time(NULL));

  Vector2d start(0,0);
  Vector2d goal(800,600);
    
  //create environment
  printf("Generating environment...\n");
  Environment *env = new Environment(800,600);
  for(int i=0; i<30; i++)
    env->addRandomConvexPolygon();
  printf("Generated!\n");
  env->saveToFile();
  delete env;
}
