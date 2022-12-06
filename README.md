I blurred image then reformatted image BGR to HSV.
For the color mask, it needs HSV values. So, I used HSV tracker for the right range of color.
![Screenshot_13](https://user-images.githubusercontent.com/80786294/206003598-2ea7705b-980e-46f1-8c53-30e2e2daecc9.png)
There is white spaces when we applied a mask in that specific color detected places.
Lastly found contours for finding biggest white space and it’s center.
![Screenshot_14](https://user-images.githubusercontent.com/80786294/206003151-db646845-8b03-41c5-b233-251c8e832365.png)
