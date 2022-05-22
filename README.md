# Hack-for-Sport

# *Objective*
Amongst all the chaos and joyous moments during a live sports match, obstructions or disturbances are caused by the manual delivery of snacks and food by the delivery person ordered by the fans spectating the match.

# *Implementation*
Our idea plans to use the void space below the seats in the stadiums and puts it to use by autonomous rail robots which will deliver the food by going in the exact row number and seat number detected. This will be done by an application interface on which the customers can order their food if in stock. The robot path will be completely covered with the casing so that they cannot be harmed or damaged by the fans in the stadium and also would not cause any difficulty or discomfort to the other seated fans, unlike the manual delivery system. Once the robot goes to the exact seat number and the food has arrived below the seat, on the hand rest, a notification will be displayed and then the person will be able to proceed for payment and receive an OTP and then from the below of the seat in the legroom area the casing will open like the doors of a metro train and the robot tray will slide out in which the food is there will be provided to the customer. Pre-payment offers will also be available which will offer benefits and catchy promos on the order, this is just a marketing strategy so that more people support the automation of such systems.

# *Application*
Automating the food delivery system will not only be useful in stadiums, but also in theatres, concerts and any other audience-based live entertainment events.

# *Approach*
Our plan for building the idea as a proper product includes visits to stadiums and understanding different seating arrangements and trying to make a generic rail robot system which can then be easily applied in any stadium and won't require specific designs. Precision and exception handling will be our aim since real-time and real-life applications of robotic systems can anytime experience an unknown event in the environment hence intelligent learning and mapping algorithms and sensors could also be included.

![Img1](https://user-images.githubusercontent.com/78747805/169707542-b0d87811-13e1-4961-83f8-dfa2481ba86d.jpeg)
![Img2](https://user-images.githubusercontent.com/78747805/169707548-b308b49d-8ef3-48d0-8a3f-047e3420cfd0.jpeg)
![Img3](https://user-images.githubusercontent.com/78747805/169707551-7f70efb0-ff3e-4ee7-af67-5b490c04998b.jpeg)
![Img4](https://user-images.githubusercontent.com/78747805/169707553-897561be-d535-45f9-9846-f45f5e711151.jpeg)
![Img5](https://user-images.githubusercontent.com/78747805/169707554-f0e902fc-dd6f-44cb-9fc1-a844e7e9bf70.jpeg)
![Img6](https://user-images.githubusercontent.com/78747805/169707555-8bb93686-b520-4501-ba69-c07447fdd8d1.jpeg)
![Img7](https://user-images.githubusercontent.com/78747805/169707556-179e1a93-709e-4126-b847-5b8b1a9ba92d.jpeg)
![Img8](https://user-images.githubusercontent.com/78747805/169707558-fbc6655b-f75c-454d-a542-1072ac44dde8.jpeg)
![Img9](https://user-images.githubusercontent.com/78747805/169707559-c6e07ff0-7495-4152-ab2e-1a9faa380696.jpeg)


# *Prototype and Demo Working*
We have placed two chairs as the two adjoining seats in the stadium in the same row and each seat has an Aruco marker attached at the bottom, where each marker has a unique ID by which each seat number can be recognised uniquely so that the robot having a top facing camera can detect the particular marker and compare the marker ids when in the camera frame to match with the seat marker ID which will be manually or automatically given as Target_ID. Until the ID of the marker in the frame and the target ID do not match the robot will keep moving forward and as soon as the robot finds the right Aruco marker having the ID equal to the target marker ID provided, in the actual situation doors like of the metro trains would open and the robot would come out and deliver the food to the customer with an alert. Once the food has been delivered, the doors would close and the robot would return to the initial position in that row.

# *What could not be done :(*
We could not implement quite a lot of things according to what we had planned: 1) Could not make the mechanism for the opening and closing of doors in front of the seats automatically like the metro train doors. 2) We wanted to first alert the customer through the app that the food has been received and only then that the doors would automatically open and the robot would come out and deliver the food, which once detected has been collected by the customer only then the robot returns and the door closes. 3) We could not make a sophisticated application to show how the food items could be purchased and how the customer would use them.

# *Simulation of the idea*
For a simulation of the idea visit this link : https://trinket.io/glowscript/c282e9c36e
