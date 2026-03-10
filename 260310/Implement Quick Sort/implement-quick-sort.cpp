#include <iostream>
#include <algorithm>

using namespace std;

// Select a proper pivot
// if Size <= 3 select leftmost element
// else select median of low, high, mid, and swap pivot with last elem in partition
int selectPivot(int arr[], int low, int high) {
    int size = high - low + 1;

    if (size <= 3) {
        return arr[high];
    }

    int mid = (low + high) / 2;

    // Find the index of the median value among low, mid, high
    int medianIdx;
    if ((arr[low] <= arr[mid] && arr[mid] <= arr[high]) || 
        (arr[high] <= arr[mid] && arr[mid] <= arr[low]))
        medianIdx = mid;
    else if ((arr[mid] <= arr[low] && arr[low] <= arr[high]) || 
             (arr[high] <= arr[low] && arr[low] <= arr[mid]))
        medianIdx = low;
    else
        medianIdx = high;

    swap(arr[high], arr[medianIdx]);

    return arr[high];
}

// Function for swapping points
void swap(int& p1, int& p2) {
    int tmp = p1;
    p1 = p2;
    p2 = tmp;
}

// Perform quick sort procedure on the partition
// Return position of pivot
int partition(int arr[], int low, int high) {
    // Select pivot and swap it with last element in partition
    int pivot = selectPivot(arr, low, high);
    
    // i represents left pointer
    int i = low - 1;
    for (int j{low}; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);

    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    // If there are 2 or more elements
    if (low < high) {
        // Find the pivot of partition
        int pos = partition(arr, low, high); 

        // Sort either side of the partition position
        quickSort(arr, low, pos - 1);
        quickSort(arr, pos + 1, high);
    }
}


int main() {
    int n;
    int arr[100000];
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Call quicksort
    quickSort(arr, 0, n - 1);

    // Print the sorted list
    for (int i{}; i < n; ++i) {
        cout << arr[i] << ' ';
    }

    return 0;
}
