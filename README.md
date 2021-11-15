# The-Eye
Coding challenge for Turing

Entities
After some consideration I decided to create 3 models to represent the scenario.
The Event is simple and will probably no change even if more scenario were to be added.
The payload and form will probably need to be adjusted to fit different values being received ny the API.
At first I considered creating a Session object, but considering that the session_id is to be created by the Application and that it is to be provided to the API, I chose not to.
I made changes to the serializers for each class in the models so that I could create them appropriately and also to present the with no empty or null fields in their JSON representations.
Basic Auth was implemented to prevent Event creation from unauthorized or bad intended users.

Constraints and Requirements
Delete, Put and Patch methods were no implemented. Considering events are not mutable once they already happended, it didn't make sense to have them in the application.
Removing such methods help reduce race conditions.

Use cases
The uses cases for the data & analytics team were implemented. The end point for listing the events will accept query params to deal with the filtering of Events.
Constraints were implemented on the models so required values are not missing on the Event, Payload or Form.
A validator was created to prevent future timestamps.
Unit teste were created aswell.

Pluses
The application is dockerized
A simple client was created to assist on testing the application