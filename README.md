# maxar_interview_question
How I solved this problem:

The first thing I decided to do was look into setting up a webservice with python.
I decided to go with Flask because I've heard good things about it from colleagues 
and the example in its documentation seemed straight forward.

Once I had a basic end point up and functioning I then moved onto solving the problem. 
I initially looked into geojson objects and briefly read the spec for it. I then stumbled 
upon geojson.io which lets you dynamically create geojson objects. I made two triangles
that overlapped and hardcoded their data into my program. I chose triangles because
they're the polygon with the least number of points--I typically prefer to solve a 
simpler version of the program fist.

So at this point I have two variables that represent geojson polygon payloads from a post request. 
I know nested deep within the object there is a list of latitude/longitude coordinates, so
my natural inclination is to extract those lists to a variable. Having done rudimentary 
object detection for a couple games that I've made with PyGame, I knew that I 
ultimately just had to compare the x and y (long and lat) values in a logically manner
that would represent boundary intersection.

So in short, I iterated through both of the coordinate lists and added their x and y values into 
their own lists, and then I created a new list of tuples per polygon with their respective
x and y values. I also decided to sort these lists to ensure that when I looped over them
that I was comparing them in some kind of logical order. Then as I iterate through 
the sorted tuples coordinate list, I realize that I'm going to have to check at least 3 or 4 points 
simultaneously in order to validate whether or not they're overlapping. 

With the way the coordinates are sorted, we'll always be checking the points from left to right. 
So using the range function to do index logic, I would check the coordinate at the end of the list (the right-most point)
e.g. [i-1] and the coordinate to the right of the current point e.g. [i+1]. And the basic pseudocode for it was 
if polygon1's longitude (x values) is less than polygon2's longitude 
and polygon1's end coordinate is larger than polygon2's longitude
and polygon1's latitude (y values) is less than polygon2's latitude 
and polygon1's end coordinate is larger than polygon2's latitude
then return true

But then I realized that there was an edge case where one of the polygons could be much smaller than the other, 
and thus technically able to reside within its x and y coordinate boundaries. Given that, I decided to google the problem 
and see if there was a library that had already solved this problem for me. 

The generous people of stack overflow let me know of a pip package called Shapely that had an intersection method. 
They also directed me to the pypi documentation for geojson where in I discovered more native methods to help me 
accomplish my goal. Instead of manually pulling out the list of coordinates from the object with dot and bracket notation 
I used to utils.coords() function which returns the same thing and is twice as easy to read. I then instantiated two Shapely
Polygons with the coordinates. Then I simply use the intersect method on them to check if they overlap, return true if 
there's an overlap, otherwise return false. 

This was a fun problem for me, it seemed easier than it ended up being. I think the main lesson I learned was
don't try to write an algorithm from scratch right away, search a little more thoroughly for good documenation/examples
next time.   
   