# Virtual-Mouse
Tiny program I made in a few days to learn how to interface OpenMV and Windows over a USB connection.

![Virtualmouse](https://user-images.githubusercontent.com/71618484/93733934-4db36700-fba5-11ea-957b-f84291a57a28.gif)

If you can zoom in, or look closely because some quality is lost in the gif, you'll be able to see the mouse on my screen moving in sync with my finger. This was pretty straighforward in terms of setup, but took a while to get working. Although there is a way to communicate over USB with Micropython and OpenMV, formating and recieving it on the windows side of things isnt that convenient. It is possible however and as you can see I demonstrated that with a simple program that passed co-ordinates of the green tape on my finger to my computer, and then mapped that to the resolution of my monitor and moved my cursor there. Sadly, I dont have access to the C# file at the moment due to myself migrating desktop PC's, but ill post that when I manage to get my hands on the file.
