#!/usr/bin/env python#*****************************************************************************
 #  Compilation:  javac LinearProbingHashST.java
 #  Execution:    java LinearProbingHashST
 #  Dependencies: StdIn.java StdOut.java
 #  
 #  Symbol table implementation with linear probing hash table.
 #
 #  % java LinearProbingHashST
 #  128.112.136.11
 #  208.216.181.15
 #  null
 #
 #
 #*****************************************************************************/

package edu.princeton.cs.algs4

#*
 #  The <tt>LinearProbingHashST</tt> class represents a symbol table of generic
 #  key-value pairs.
 #  It supports the usual <em>put</em>, <em>get</em>, <em>contains</em>,
 #  <em>delete</em>, <em>size</em>, and <em>is-empty</em> methods.
 #  It also provides a <em>keys</em> method for iterating over all of the keys.
 #  A symbol table implements the <em>associative array</em> abstraction:
 #  when associating a value with a key that is already in the symbol table,
 #  the convention is to replace the old value with the new value.
 #  Unlike {@link java.util.Map}, this class uses the convention that
 #  values cannot be <tt>null</tt>&mdash;setting the
 #  value associated with a key to <tt>null</tt> is equivalent to deleting the key
 #  from the symbol table.
 #  <p>
 #  This implementation uses a linear probing hash table. It requires that
 #  the key type overrides the <tt>equals()</tt> and <tt>hashCode()</tt> methods.
 #  The expected time per <em>put</em>, <em>contains</em>, or <em>remove</em>
 #  operation is constant, subject to the uniform hashing assumption.
 #  The <em>size</em>, and <em>is-empty</em> operations take constant time.
 #  Construction takes constant time.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/34hash">Section 3.4</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #  For other implementations, see {@link ST}, {@link BinarySearchST},
 #  {@link SequentialSearchST}, {@link BST}, {@link RedBlackBST}, and
 #  {@link SeparateChainingHashST},
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #/
public class LinearProbingHashST<, Value>:
    private static final INIT_CAPACITY = 4

    private N;           # number of key-value pairs in the symbol table
    private M;           # size of linear probing table
    private keys;      # the keys
    private Value[] vals;    # the values


    #*
     # Initializes an empty symbol table.
     #/
    public LinearProbingHashST():
        this(INIT_CAPACITY)

    #*
     # Initializes an empty symbol table of given initial capacity.
     # @param capacity the initial capacity
     #/
    public LinearProbingHashST(int capacity):
        M = capacity
        keys = ([])   new [M]
        vals = (Value[]) new [M]

    #*
     # Returns the number of key-value pairs in this symbol table.
     # @return the number of key-value pairs in this symbol table
     #/
    def size():
        return N

    #*
     # Is this symbol table empty?
     # @return <tt>true</tt> if this symbol table is empty and <tt>false</tt> otherwise
     #/
    def isEmpty():
        return size() == 0

    #*
     # Does this symbol table contain the given key?
     # @param key the key
     # @return <tt>true</tt> if this symbol table contains <tt>key</tt> and
     #     <tt>false</tt> otherwise
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def contains( key):
        return get(key) is not None

    # hash function for keys - returns value between 0 and M-1
    def _hash( key):
        return (key.hashCode() & 0x7fffffff) % M

    # resize the hash table to the given capacity by re-hashing all of the keys
    def _resize(int capacity):
        LinearProbingHashST<, Value> temp = new LinearProbingHashST<, Value>(capacity)
        for (int i = 0; i < M; i += 1):
            if keys[i] is not None):
                temp.put(keys[i], vals[i])
        keys = temp.keys
        vals = temp.vals
        M    = temp.M

    #*
     # Inserts the key-value pair into the symbol table, overwriting the old value
     # with the new value if the key is already in the symbol table.
     # If the value is <tt>null</tt>, this effectively deletes the key from the symbol table.
     # @param key the key
     # @param val the value
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def put( key, Value val):
        if val is None):
            delete(key)
            return

        # double table size if 50% full
        if N >= M/2) resize(2*M)

        i
        for (i = hash(key); keys[i] is not None; i = (i + 1) % M):
            if keys[i].equals(key)):
                vals[i] = val
                return
        keys[i] = key
        vals[i] = val
        N += 1

    #*
     # Returns the value associated with the given key.
     # @param key the key
     # @return the value associated with the given key if the key is in the symbol table
     #     and <tt>null</tt> if the key is not in the symbol table
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def get( key):
        for (int i = hash(key); keys[i] is not None; i = (i + 1) % M) 
            if keys[i].equals(key))
                return vals[i]
        return None

    #*
     # Removes the key and associated value from the symbol table
     # (if the key is in the symbol table).
     # @param key the key
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def delete( key):
        if !contains(key)) return

        # find position i of key
        i = hash(key)
        while (!key.equals(keys[i])):
            i = (i + 1) % M

        # delete key and associated value
        keys[i] = None
        vals[i] = None

        # rehash all keys in same cluster
        i = (i + 1) % M
        while (keys[i] is not None):
            # delete keys[i] an vals[i] and reinsert
               keyToRehash = keys[i]
            Value valToRehash = vals[i]
            keys[i] = None
            vals[i] = None
            N -= 1
            put(keyToRehash, valToRehash)
            i = (i + 1) % M

        N -= 1

        # halves size of array if it's 12.5% full or less
        if N > 0 and N <= M/8) resize(M/2)

        assert check()

    #*
     # Returns all keys in the symbol table as an <tt>Iterable</tt>.
     # To iterate over all of the keys in the symbol table named <tt>st</tt>,
     # use the foreach notation: <tt>for (Key key : st.keys())</tt>.
     # @return all keys in the sybol table as an <tt>Iterable</tt>
     #/
    def keys():
        Queue<> queue = new Queue<>()
        for (int i = 0; i < M; i += 1)
            if keys[i] is not None) queue.enqueue(keys[i])
        return queue

    # integrity check - don't check after each put() because
    # integrity not maintained during a delete()
    def _check():

        # check that hash table is at most 50% full
        if M < 2*N):
            System.err.println("Hash table size M = " + M + "; array size N = " + N)
            return False

        # check that each key in table can be found by get()
        for (int i = 0; i < M; i += 1):
            if keys[i] is None) continue
            elif (get(keys[i]) != vals[i]):
                System.err.println("get[" + keys[i] + "] = " + get(keys[i]) + "; vals[i] = " + vals[i])
                return False
        return True


    #*
     # Unit tests the <tt>LinearProbingHashST</tt> data type.
     #/
    def main(String[] args): 
        LinearProbingHashST<String, Integer> st = new LinearProbingHashST<String, Integer>()
        for (int i = 0; !StdIn.isEmpty(); i += 1):
            String key = StdIn.readString()
            st.put(key, i)

        # print keys
        for (String s : st.keys()) 
            prt.write(s + " " + st.get(s))

#*****************************************************************************
 #  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
 #
 #  This file is part of algs4.jar, which accompanies the textbook
 #
 #      Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
 #      Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
 #      http://algs4.cs.princeton.edu
 #
 #
 #  algs4.jar is free software: you can redistribute it and/or modify
 #  it under the terms of the GNU General Public License as published by
 #  the Free Software Foundation, either version 3 of the License, or
 #  (at your option) any later version.
 #
 #  algs4.jar is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with algs4.jar.  If not, see http://www.gnu.org/licenses.
 #*****************************************************************************/
