#include <iostream> 
#include <vector>
using namespace std;


//function

int binarySearch(vector<int> array, int target){
    int start = 0, end = array.size()-1;


    while (start <= end ){
        int mid = start + (end - start )/ 2;

        if (target > array[mid]){
            start = mid + 1;

        }else if (target < array[mid]){
            end = mid - 1;
        }else{
            return mid;
        }
    }


    return -1; //if there is no target value in the array  then return -1
}

int main (){
    vector <int> array1 = {-1, 0, 3, 4, 5, 6, 9, 12};
    int target1 = 6;

    cout<< binarySearch (array1, target1) <<endl;

    vector <int> array2 = {-1, 0, 3, 4, 7, 6, 9, 12};
    int target2 = 0;



    return 0;


}