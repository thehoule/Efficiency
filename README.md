Efficiency
==========

Determine efficiency for high order applications.

Use Newton Cotes:
-----------------

### Constant Interpolant(Composite Midpoint Rule):
This rule approximates the integral by using the midpoints of the integral itself. It does this by using a
rectangle at the midpoint of the integral and then dividing them up into smaller, easier approximating
rectangles to come to a close and more accurate approximation. The step sizes to test the approximation accuracy is run through the equation itself:

![](http://turing.une.edu.au/~amth247/Lectures_2003/Lecture_17/lecture/img22.gif "Composite Midpoint Rule") 

### Linear Interpolant(Composite Trapezoid Rule):
This rule approximates the integral by using the area of a trapezoid and then dividing that trapezoid into
much smaller trapezoids to get an extremely accurate approximation. This rule is extremely efficient with
very little curvature of the integral. This equation is run through multiple step sizes to determine the
accuracy of it compared against the others. The equation itself is the following:

![](http://upload.wikimedia.org/math/f/c/c/fcc7b80f5e85dce8b8a262ee9ce83223.png "Composite Trapezoid Rule")

### Quadratic Interpolant (Composite Simpson Formula):
This approximates the integral by using the midpoint between the integral range, then using a quadratic
polynomial that interpolates with those three points. Then using the new equation the integral is
approximated by approximating the integral of the interpolating polynomial. This rule is extremely efficient
with curvature. With it’s efficiency it is also quite accurate as well. The equation itself is the following:

![](http://upload.wikimedia.org/math/a/c/2/ac281e21c702c7a01b4270ada92baa27.png "Composite Simpson Formula")


Use Gaussian Methods:
---------------------

###Gaussian Quadrature:

![](http://upload.wikimedia.org/math/1/b/a/1ba3e9e642523eb58f98f00539aafd60.png "Gaussian Quadrature")

### Legendre Polynomial Table:
The Legendre polynomial table has the gaussian quadrature points and weights for a small N. The
gaussian quadrature rarely uses sizes for N larger than 5. The values from the polynomial table are run
through the integral equation to determine the accuracy of approximation of the Legendre table against the
Chebyshev polynomial table. The Legendre table is as follows:

![](http://www.deltaquants.com/assets/images/Legendre%20polynomialsf-5.jpg "Legendre Polynomial Table")

### Chebyshev Polynomial Table:
The Chebyshev polynomial table also provides the gaussian quadrature points and weights for small size
N. The values from the polynomial table are run through the integral equation to determine the accuracy of
approximation of the Chebyshev table against the Legendre polynomial table. The Chebyshev table is populated as
follows with the weight pairs:

![](http://upload.wikimedia.org/math/5/1/8/518d176892c2edaa19236135029bd39b.png "Set Pair")

![](http://upload.wikimedia.org/math/0/c/9/0c91407b3f3801c08124305d8655b085.png "Weight Pair")
