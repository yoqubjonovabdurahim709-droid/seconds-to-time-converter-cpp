#include <iostream>
using namespace std;

void convertTime (int totalSeconds){
    int hours, seconds, minutes ;
    int remSeconds;

    hours = totalSeconds / 3600;

    remSeconds = totalSeconds % 3600;

    minutes = remSeconds / 60;

    seconds = remSeconds % 60;

    cout << "Hours: " << hours << endl;
    
    cout << "Minutes: " << minutes << endl;
    cout << "Seconds: " << seconds << endl;
}

int main (){
    int totalSeconds;
    do{
        cout << "Enter total seconds: " << endl;
        cin >> totalSeconds;

        if (totalSeconds < 0){
            cout << "Please enter non - negative number of seconds !" << endl;
        }

    }while(totalSeconds < 0);

 convertTime( totalSeconds);
return 0;

}
