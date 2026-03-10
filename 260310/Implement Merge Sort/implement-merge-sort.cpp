#include <iostream>

using namespace std;

void merge(int arr[], int mergedArr[], int low, int mid, int high) {
    int i = low, 
        j = mid + 1,
        k = low;

    while (i <= mid && j <= high) {
        if (arr[i] <= arr[j]) {
            mergedArr[k] = arr[i];
            i++;
            k++;
        } else {
            mergedArr[k] = arr[j];
            j++;
            k++;
        }
    }

    while (i <= mid) {
        mergedArr[k] = arr[i];
        i++;
        k++;
    }

    while (j <= high) {
        mergedArr[k] = arr[j];
        j++;
        k++;
    }

    for (int idx{low}; idx <= high; idx++) {
        arr[idx] = mergedArr[idx];
    }
}

void mergeSort(int arr[], int mergedArr[], int low, int high) {
    if (low >= high) return;

    int mid = (low + high) / 2;
    mergeSort(arr, mergedArr, low, mid);
    mergeSort(arr, mergedArr, mid + 1, high);
    merge(arr, mergedArr, low, mid, high);
}

int n;
int arr[100000];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Perform merge sort
    int mergedArr[n];
    mergeSort(arr, mergedArr, 0, n - 1);

    // Print result
    for (int i{}; i < n; ++i) {
        cout << mergedArr[i] << ' ';
    }

    return 0;
}


