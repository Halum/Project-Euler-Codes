#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<utility>
#include<functional>
#include<bitset>
#include<deque>
#include<set>
#include<algorithm>
#include<ctime>
#include<string>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<map>  // END OF LIBRARY
#define sdum scanf("%c",&dummy)
#define pn printf("\n")
#define sn scanf("\n")
#define eps 1e-12
#define SIZE 20000000
//---------------------------------------------------->
typedef unsigned long long int ULL;
typedef long long int LL;
typedef unsigned int UI;
typedef long double LD;
using namespace std;
int T, len, N, sum, x, y, cary, ans, temp, total, MAX, MIN;
char ch, dum, *ptr;
bool check;
//---------------------------------------------------->
bool prime[SIZE];
int sieve( )
{
    memset(prime, true, sizeof prime);
    sum = 2;

    int root = sqrt( SIZE );

    for( int i = 3; i <= root; i += 2 )
    {
        if( prime[i] )
        {
            for( int j = i*i; j < SIZE; j += 2*i )
                prime[j] = false;
        }
    }

    for(int i = 3; i <= 2000000; i += 2)
        if( prime[i] )
            sum += i;


    return sum;
}

//---------------------------------------------------->
int main()    //
{
    register int i, j=1, k, l=0;
    //freopen("A.txt","r",stdin);
    //freopen("B.txt","w",stdout);
//---------------------------------------------------->
    cout << sieve() << endl;



    return 0;
}


