using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Net;

class Program
{
    static string[] calls = {
        "Kelly's Eye - 1", "One little duck - 2", "Cup of tea - 3", "Knock at the door - 4", "Man alive - 5", "Half a dozen - 6",
        "Lucky for some - 7", "Garden gate - 8", "Doctor's Orders - 9", "Rishi's Den - 10", "Legs eleven - 11", "One dozen - 12",
        "Unlucky for some - 13", "Valentine's Day - 14", "Young and keen - 15", "Never been kissed - 16", "Dancing Queens - 17",
        "Coming of age - 18", "Goodbye teens - 19", "One Score - 20", "Royal Salute - 21", "Two little ducks - 22", "Thee and me - 23",
        "Two dozen - 24", "Duck and dive - 25", "Half a crown - 26", "Duck and a crutch - 27", "In a state - 28", "Rise and shine - 29",
        "Dirty Gertie - 30", "Get up and run - 31", "Buckle my shoe - 32", "Dirty knee - 33", "Ask for more - 34", "Jump and jive - 35",
        "Three dozen - 36", "More than eleven - 37", "Christmas cake - 38", "Steps - 39", "Life begins - 40", "Time for fun - 41",
        "Winnie the Pooh - 42", "Down on your knees - 43", "Droopy Drawers - 44", "Halfway there - 45", "Up to tricks - 46",
        "Four and seven - 47", "Four dozen - 48", "PC - 49", "It's a bullseye! - 50", "Tweak of the thumb - 51", "Chicken Vindaloo - 52",
        "Stuck in the tree - 53", "Man at the door - 54", "All the fives - 55", "Shotts bus - 56", "Heinz Varieties - 57",
        "Make them wait - 58", "Brighton Line - 59", "Grandma's getting frisky - 60", "Bakers bun - 61", "Tickety-Boo - 62",
        "Tickle me - 63", "Almost retired - 64", "Retirement age - 65", "Clickety click - 66", "Stairway to Heaven - 67",
        "Pick a mate - 68", "Anyway up - 69", "Three score and ten - 70", "Bang on the drum - 71", "Danny La Rue - 72",
        "Queen bee - 73", "Hit the floor - 74", "Strive and strive - 75", "Trombones - 76", "Two little crutches - 77",
        "Heaven's gate - 78", "One more time - 79", "Eight and blank - 80", "Stop and run - 81", "Straight on through - 82",
        "Time for tea - 83", "Give me more - 84", "Staying alive - 85", "Between the sticks - 86", "Torquay in Devon - 87",
        "Two fat ladies - 88", "Nearly there - 89", "Top of the shop - 90"
    };

    static string CURRENT_VERSION = "10.0.0";

    static void Main(string[] args)
    {
        Console.Title = "Bingo Caller " + CURRENT_VERSION;
        Console.WriteLine("Welcome to Bingo Caller version " + CURRENT_VERSION);
        System.Threading.Thread.Sleep(1000);
        Console.WriteLine("After you type a value, press Enter to submit it.");
        System.Threading.Thread.Sleep(1000);
        app();
        Ending();
        ExitProgram();
    }

    static void ExitProgram()
    {
        // exit();
        System.Environment.Exit(0);
        // Process.Start(@"C:\Program Files (x86)\Bingo Caller\bin\kill.bat");
    }

    static void ReRun()
    {
        int numberOfRounds;
        string numberOfRoundsAsString;

        try
        {
            Console.Write("How many numbers would you like generated for this round: ");
            numberOfRounds = int.Parse(Console.ReadLine());
        }
        catch (FormatException)
        {
            Console.Write("Please enter a valid number: ");
            numberOfRounds = int.Parse(Console.ReadLine());
        }

        numberOfRoundsAsString = numberOfRounds.ToString();

        Console.Write("Are you sure you want to have " + numberOfRoundsAsString + " goes? Enter 'Y' for yes and 'N' for no: ");
        string confirmRounds = Console.ReadLine().ToLower();

        while (confirmRounds != "y" && confirmRounds != "n")
        {
            Console.Write("Invalid input. Enter 'Y' for yes and 'N' for no: ");
            confirmRounds = Console.ReadLine().ToLower();
        }

        while (confirmRounds == "n")
        {
            try
            {
                Console.Write("How many numbers would you like generated for this game? ");
                numberOfRounds = int.Parse(Console.ReadLine());
            }
            catch (FormatException)
            {
                Console.Write("Please enter a valid number: ");
                numberOfRounds = int.Parse(Console.ReadLine());
            }

            numberOfRoundsAsString = numberOfRounds.ToString();

            Console.Write("Are you sure you want " + numberOfRoundsAsString + " goes? Enter 'Y' for yes and 'N' for no: ");
            confirmRounds = Console.ReadLine().ToLower();
        }

        Console.WriteLine("Let's play bingo!");
        Console.Write("Press Enter to get your first number, and again after every number called: ");
        string ready = Console.ReadLine();

        Random random = new Random();
        List<string> alreadyCalled = new List<string>();
        int x = 0;
        int actRound = numberOfRounds;

        while (x < numberOfRounds)
        {
            string nextNumber;
            do
            {
                nextNumber = calls[random.Next(calls.Length)];
            }
            while (alreadyCalled.Contains(nextNumber));

            alreadyCalled.Add(nextNumber);
            Console.WriteLine(nextNumber);
            actRound--;
            Console.WriteLine("You have " + actRound + " goes left");
            Console.ReadLine();
            x++;
        }

        Console.WriteLine("You have reached your selected amount of " + numberOfRoundsAsString + " goes.");
        System.Threading.Thread.Sleep(500);
    }

    


    static void app()
    {
        Console.WriteLine("Would you like to contact support?");
        Console.Write("Enter 'Y' for yes or 'N' for no: ");
        string support = Console.ReadLine().ToLower();

        if (support == "y")
        {
            Console.Write("Enter 'T' for ticket creation or 'E' for email: ");
            string questionEmail = Console.ReadLine().ToLower();

            if (questionEmail == "t")
            {
                Process.Start("https://bcd.rf.gd/support/");
                ExitProgram();
            }
            else if (questionEmail == "e")
            {
                Process.Start("mailto:support@bingocaller.me");
                ExitProgram();
            }
        }
        else if (support == "n")
        {
            int numberOfRounds;
            string numberOfRoundsAsString;

            try
            {
                Console.Write("How many numbers would you like generated for this round: ");
                numberOfRounds = int.Parse(Console.ReadLine());
            }
            catch (FormatException)
            {
                Console.Write("Please enter a valid number: ");
                numberOfRounds = int.Parse(Console.ReadLine());
            }

            numberOfRoundsAsString = numberOfRounds.ToString();

            Console.Write("Are you sure you want " + numberOfRoundsAsString + " goes? Enter 'Y' for yes and 'N' for no: ");
            string confirmRounds = Console.ReadLine().ToLower();

            while (confirmRounds != "y" && confirmRounds != "n")
            {
                Console.Write("Invalid input. Enter 'Y' for yes and 'N' for no: ");
                confirmRounds = Console.ReadLine().ToLower();
            }

            while (confirmRounds == "n")
            {
                try
                {
                    Console.Write("How many numbers would you like generated for this game? ");
                    numberOfRounds = int.Parse(Console.ReadLine());
                }
                catch (FormatException)
                {
                    Console.Write("Please enter a valid number: ");
                    numberOfRounds = int.Parse(Console.ReadLine());
                }

                numberOfRoundsAsString = numberOfRounds.ToString();

                Console.Write("Are you sure you want " + numberOfRoundsAsString + " goes? Enter 'Y' for yes and 'N' for no: ");
                confirmRounds = Console.ReadLine().ToLower();
            }

            Console.WriteLine("Let's play bingo!");
            Console.Write("Press Enter to get your first number, and after every number called: ");
            string ready = Console.ReadLine();

            Random random = new Random();
            List<string> alreadyCalled = new List<string>();
            int x = 0;
            int actRound = numberOfRounds;

            while (x < numberOfRounds)
            {
                string nextNumber;
                do
                {
                    nextNumber = calls[random.Next(calls.Length)];
                }
                while (alreadyCalled.Contains(nextNumber));

                alreadyCalled.Add(nextNumber);
                Console.WriteLine(nextNumber);
                actRound--;
                Console.WriteLine("You have " + actRound + " goes left");
                Console.ReadLine();
                x++;
            }

            Console.WriteLine("You have reached your selected amount of " + numberOfRoundsAsString + " goes.");
            System.Threading.Thread.Sleep(500);
        }
    }

    static void Ending()
    {
        Console.Write("Would you like to play Bingo Caller again? Enter 'Y' for yes and 'X' to exit: ");
        string again = Console.ReadLine().ToLower();

        while (again != "y" && again != "x")
        {
            Console.Write("Invalid input. Enter 'Y' for yes and 'X' to exit: ");
            again = Console.ReadLine().ToLower();
        }

        while (again == "y")
        {
            ReRun();
            Console.Write("Would you like to play Bingo Caller again? Enter 'Y' for yes and 'X' to exit: ");
            again = Console.ReadLine().ToLower();
        }

        while (again != "y" && again != "x")
        {
            Console.Write("Invalid input. Enter 'Y' for yes and 'X' to exit: ");
            again = Console.ReadLine().ToLower();
        }

        if (again == "x")
        {
            Console.WriteLine("Goodbye, and thank you for playing Bingo Caller!");
            System.Threading.Thread.Sleep(1210);
        }
    }
}
