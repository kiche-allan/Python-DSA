array is a collection of data of the same type whereas a linked list is a collection of the same data type stored sequentially and connected through pointers
Inase of lists, the data elements are stored in diffeent memory allocations whereas the array elements are stored in contigous memory locations
-an array stores data of the same type and each data element in the array is stored in contigous memory locations. Storing multiple data values of the same type makes it easier and faster to compute the positio]n of any elemt in the array using offset and base address
- To store , traverse and access array elements is very fast as compared to lists sice elements can be accessed randomly using their index positions whereas o=in casee of a linked list, the elements can be accessed sequentially. 
Therefore, if the data to be stored in the array is large and the system has
low memory, the array data structure will not be a good choice to store the
data because it is difficult to allot a large block of memory locations. The
array data structure has further limitations in that it has a static size that has
to be declared at the time of creation.
In addition, the insertion and deletion operations in array data structures are
slow as compared to linked lists. This is because it is difficult to insert an
element in an array at a given location since all data elements after that
desired position must be shifted and then new elements inserted in between.
Thus, array data structures are suitable when we want to do a lot of
accessing of elements and fewer insertion and deletion operations, whereas
linked lists are suitable in applications where the size of the list is not fixed,
and a lot of insertion and deletion operations will be required.