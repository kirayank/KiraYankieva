#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int buffer;
    ifstream text("numbers.txt");
    vector <int> all_numbers;
    vector <int> memory;
    int max = -1,min = 32769;

    while(!text.eof())
    {
        text >> buffer;
        cout << buffer << endl;
        all_numbers.insert(all_numbers.end(),buffer);

        for(int k=0;k<all_numbers.size();++k)
        {
            if(max<all_numbers[k])
                max = all_numbers[k];
            if(min>all_numbers[k])
                min = all_numbers[k];
        }


        for(int r=min;r<=max;++r)
            memory.insert(memory.end(),r);

        for(int y=0; y<memory.size();++y)
        {
            for(int g=0;g<all_numbers.size();++g)
            {
                if(memory[y]==all_numbers[g])
                {
                    memory.erase(memory.begin()+y);
                }

            }
        }

        if(memory.empty())
            cout << "Message "<< min << "-" << max << " recieved RIGHT" << endl;
        else
        {
            cout << "Message "<< min << "-" << max << " received WRONG: ";
            for(int i=0; i<memory.size();++i)
                cout << memory[i] << " ";
            cout << " are missing" << endl;
        }
        memory.clear();
    }


    cout << min << " " << max;
    text.close();
    return 0;
}
