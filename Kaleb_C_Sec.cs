using System.Collections.Generic;
using System.Text;


public static class C_Security_Demo
    {
        private static string SanitizeData(string userData)
        {
            // declaring what characters are "Not Allowed"
            List<char> disAllowList = new List<char>();
            char[] disAllowChars = {'/', '\\', '-', ':'};
            disAllowList.Add('/');
            disAllowList.Add('\\');
            disAllowList.Add('-');
            disAllowList.Add(':');
            
            // declaring what will be sent back
            string returnString = "";

            //checking to see if any characters are banned
            for(int i=0; i < userData.Length; i++)
            {
                if(userData[i] == disAllowList[0] || userData[i] == disAllowList[1] || 
                   userData[i] == disAllowList[2] || userData[i] == disAllowList[3])
                {
                    return returnString;
                }
                else
                {
                    var input = userData[i];
                    string stringInput = Char.ToString(input);
                    returnString = returnString.Insert(returnString.Length, stringInput);
                }
            }
            return returnString;
        }

        private static Boolean FindDifference(string file1, string file2)
        {
            string filetext1;
            string filetext2;
            var fileStream = new FileStream(file1, FileMode.Open, FileAccess.Read);
            using (var streamReader = new StreamReader(fileStream, Encoding.Default))
            {
                filetext1 = streamReader.ReadToEnd();
            }

            var fileStream2 = new FileStream(file2, FileMode.Open, FileAccess.Read);
            using (var streamReader = new StreamReader(fileStream2, Encoding.Default))
            {
                filetext2 = streamReader.ReadToEnd();
            }

            if (filetext1 == filetext2)
            {
                return true;
            }

            return false;
        }
        
        private static void Main() // running examples here
        {
            
            // Sanitizing the data problem
            string oldData = "fireball:--";
            Console.Write("Before Data: ");
            Console.WriteLine(oldData);
            string betterData = SanitizeData(oldData);
            Console.Write("After Sanitizing: ");
            Console.WriteLine(betterData);
            Console.WriteLine();

            // determining if two files differ so that updates can be determined
            Console.WriteLine("------------");
            Console.WriteLine();

            string filepath = "test.txt";
            string filepath2 = "test2.txt";
            Boolean isSame = FindDifference(filepath, filepath2);
            if (isSame == true)
            {
                Console.WriteLine("The Contents are the same. No update needed");
            }

            if (isSame == false)
            {
                Console.WriteLine("The contents differ. Update required");
            }
        }
    }