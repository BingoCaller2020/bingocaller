using System;
using System.Diagnostics;
using System.ComponentModel;

namespace MyProcessSample
{
    class MyProcess
    {
        public static void Main(string[] args)
        {
            Console.Title = "Possible Colour Choices";
            Console.WriteLine("Press the 'Enter' key to view the next colour choice");
            Console.ReadKey();
            Console.WriteLine(" Enter '07' for white text on a black background");
            Console.ReadKey();
            Console.WriteLine(" Enter '02' for green text on a black background");
            Console.ReadKey();
            Console.WriteLine(" Enter '04' for red text on a black background");
            Console.ReadKey();
            Console.WriteLine(" Enter '01' for blue text on a black background");
            Console.ReadKey();
            Console.WriteLine(" Enter '08' for grey text on a black background");
            Console.ReadKey();
            Console.WriteLine(" Enter '05' for purple text on a black background");
            Console.ReadKey();
            Console.WriteLine(" Enter '06' for yellow text on a black background");
            Console.ReadKey();
            using (Process myProcess = new Process())
            {
                myProcess.StartInfo.UseShellExecute = true;
                // You can start any process, HelloWorld is a do-nothing example.
                myProcess.StartInfo.FileName = "C:\\Program Files (x86)\\Bingo Caller\\Bingo Caller.exe";
                myProcess.StartInfo.CreateNoWindow = true;
                myProcess.Start();
                // This code assumes the process you are starting will terminate itself.
                // Given that is is started without a window so you cannot terminate it
                // on the desktop, it must terminate itself or you can do it programmatically
                // from this application using the Kill method.
            }
        }
    }
}

