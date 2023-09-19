# circle-radius-area
## Python library that can calculate the area of ​​a circle by radius and of a triangle by three sides.

1. Unit Tests
   
This Python library is equipped with a suite of unit tests to ensure the correctness of its functionality. 

To run the unit tests, you can execute the test script provided in the repository. The tests cover a range of scenarios, including valid and invalid input values, as well as edge cases to verify the library's robustness.

2. Ease of Adding Other Shapes
   
One of the key design principles of the library is its extensibility. Adding support for new geometric shapes is straightforward, making it easy to expand the library's capabilities beyond circles and triangles. To include additional shapes, you can simply define new methods within the AreaCalc class, following a similar pattern to the existing methods.

3. Runtime Determination of Shape Type

The library offers the flexibility to calculate the area of a geometric figure without requiring prior knowledge of the figure's type at compile-time. This means that you can input the necessary parameters, such as the radius for a circle or the sides for a triangle, and the library will determine the appropriate calculation method dynamically. 

4. Checking if a Triangle Is Right-Angled
   
The library includes a method called is_triangle_orthogonal that allows you to check whether a given set of sides forms a right-angled triangle. The method employs the Pythagorean theorem to make this determination, providing a convenient way to verify the characteristics of triangles in your applications.
