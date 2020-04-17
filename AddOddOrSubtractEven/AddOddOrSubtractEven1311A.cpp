#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, a, b;
    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> a >> b;
        int diff = b - a;

        if(diff == 0)
        {
            cout << 0;
        }
        else if(diff > 0 && diff % 2 == 1)
        {
            cout << 1;
        }
        else if(diff > 0 && diff % 2 == 0)
        {
            cout << 2;
        }
        else if(diff < 0 && diff % 2 == -1)
        {
            cout << 2;
        }
        else if(diff < 0 && diff % 2 == 0)
        {
            cout << 1;
        }
        cout << endl;
    }
}