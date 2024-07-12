import java.io.*;
import java.util.*;

class xor {
    static int countTriplets(int[] a, intn) {
        ArrayList<Integer> s = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            s.add(a[i]);
        }

        int count = 0;
        // traverse for all i, j pairs
        // such that j>i
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xr = a[i] + a[j];
                if (s.contains(xr) && xr != a[i] && xr != a[j]) {
                    count++;
                }
            }
        }

        return count / 3;
    }
}