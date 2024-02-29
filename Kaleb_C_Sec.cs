using System.Collections.Generic;


{
    public static class C#_Security_Demo
    {
        private static string SanitizeData(string userData)
        {
            // declaring what characters are "Not Allowed"
            List<> disAllowList = new List<>();
            string[] disAllowChars = {'/', '\\', '--', ':'};
            
            // declaring what will be sent back
            string returnString;

            //checking to see if any characters are banned
            foreach(character in userData)
            {
                if(character in disAllowChars)
                {
                    return returnString;
                }
                else
                {
                    returnString += character;
                }
            }
            return returnString;
        }
    private static void Main()
    {


        // Sanitizing the data problem
        var oldData = "fireball:--";
        Console.Write("Before Data: ");
        Console.Writeline(oldData);
        var betterData = SanitizeData(oldData);
        Console.Writeline("After Sanitizing: ");
        Console.WriteLine(betterData);

        // Other problem that needs to be solved
    }
    
    
    }


}