<template>
  <div class="container mx-auto">
    <h2 class="text-3xl font-bold mb-4">Student List</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="student in students" :key="student.StudentID" class="border p-4 rounded shadow">
        <h3 class="text-xl font-bold">{{ student.Firstname }} {{ student.Lastname }}</h3>
        <p class="text-gray-600">{{ student.Email }}</p>
        <div class="mt-4 flex justify-end">
          <button @click="editStudent(student)" class="mr-2 px-4 py-2 bg-blue-500 text-white rounded">Edit</button>
          <button @click="deleteStudent(student.StudentID)" class="px-4 py-2 bg-red-500 text-white rounded">Delete</button>
        </div>
      </div>
    </div>

    <!-- Add/Edit Student Form -->
    <form v-if="editMode" @submit.prevent="updateStudent" class="mt-8">
      <h3 class="text-2xl font-bold mb-4">Edit Student</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label for="editFirstname" class="mb-2 block">First Name:</label>
          <input type="text" id="editFirstname" v-model="editStudent.Firstname" class="border rounded px-4 py-2 w-full">
        </div>
        <div>
          <label for="editLastname" class="mb-2 block">Last Name:</label>
          <input type="text" id="editLastname" v-model="editStudent.Lastname" class="border rounded px-4 py-2 w-full">
        </div>
      </div>
      <div class="mt-4">
        <label for="editEmail" class="mb-2 block">Email:</label>
        <input type="email" id="editEmail" v-model="editStudent.Email" class="border rounded px-4 py-2 w-full">
      </div>
      <div class="mt-4">
        <button type="submit" class="px-6 py-3 bg-green-500 text-white rounded">Update Student</button>
        <button type="button" @click="cancelEdit" class="ml-2 px-6 py-3 bg-gray-500 text-white rounded">Cancel</button>
      </div>
    </form>

    <!-- Add Student Form -->
    <form v-else @submit.prevent="addStudent" class="mt-8">
      <h3 class="text-2xl font-bold mb-4">Add Student</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label for="firstname" class="mb-2 block">First Name:</label>
          <input type="text" id="firstname" v-model="newStudent.Firstname" class="border rounded px-4 py-2 w-full">
        </div>
        <div>
          <label for="lastname" class="mb-2 block">Last Name:</label>
          <input type="text" id="lastname" v-model="newStudent.Lastname" class="border rounded px-4 py-2 w-full">
        </div>
      </div>
      <div class="mt-4">
        <label for="email" class="mb-2 block">Email:</label>
        <input type="email" id="email" v-model="newStudent.Email" class="border rounded px-4 py-2 w-full">
      </div>
      <div class="mt-4">
        <button type="submit" class="px-6 py-3 bg-green-500 text-white rounded">Add Student</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const students = ref([]);
const newStudent = ref({ Firstname: '', Lastname: '', Email: '' });
const editStudent = ref(null);
const editMode = ref(false);

const fetchStudents = () => {
  axios.get('http://127.0.0.1:8000/students')
    .then(response => {
      students.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching students:', error);
    });
};

const addStudent = () => {
  axios.post('http://127.0.0.1:8000/students', newStudent.value)
    .then(response => {
      console.log('Student added successfully:', response.data);
      newStudent.value = { Firstname: '', Lastname: '', Email: '' };
      fetchStudents(); // Refresh the student list
    })
    .catch(error => {
      console.error('Error adding student:', error);
    });
};

const startEdit = (student) => {
  editStudent.value = { ...student };
  editMode.value = true;
};

const cancelEdit = () => {
  editMode.value = false;
  editStudent.value = null;
};

const updateStudent = () => {
  axios.put(`http://127.0.0.1:8000/students/${editStudent.value.StudentID}`, editStudent.value)
    .then(response => {
      console.log('Student updated successfully:', response.data);
      editMode.value = false;
      fetchStudents(); // Refresh the student list
    })
    .catch(error => {
      console.error('Error updating student:', error);
    });
};

const deleteStudent = (studentId) => {
  axios.delete(`http://127.0.0.1:8000/students/${studentId}`)
    .then(response => {
      console.log('Student deleted successfully:', response.data);
      fetchStudents();
    })
    .catch(error => {
      console.error('Error deleting student:', error);
    });
};

onMounted(fetchStudents);
</script>

