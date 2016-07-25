using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Item44c2Exercises
{
    class Program
    {
        static void whileWrong()
        {
            var constant = "y";
            Console.WriteLine("What is the command keyword to exit a loop in C#?");
            Console.WriteLine("a. int");
            Console.WriteLine("b. continue");
            Console.WriteLine("c. break");
            Console.WriteLine("d.exit");
            while (constant == "y")
            {
                Console.WriteLine("Enter your choice:");
                var ans = Console.ReadLine();
                if (ans == "c")
                {
                    Console.WriteLine("Congrats");
                    constant = "x";
                }
                else
                {
                    if (ans == "a" || ans == "b" || ans == "d")
                    {
                        Console.WriteLine("Incorrect! \n Again? Press y to continue.");
                        constant = Console.ReadLine();
                    }
                }
            }
        }
        static void doAscii()
        {
            int x = 123;
            do
            {
                char character = Convert.ToChar(x);
                Console.WriteLine("ASCII code{0} = character {1}", x, character);
                x--;
            }
            while (x >= 1 && x <= 122);
        }
        static void Main(string[] args)
        {
            Program.whileWrong();
            Program.doAscii();
        }
    }
}
