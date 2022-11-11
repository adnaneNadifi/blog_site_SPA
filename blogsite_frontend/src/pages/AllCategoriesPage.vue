<template>
    <div >

        <div class="q-pa-md w-[400px]" >

        <q-form
            ref="myForm"
            class="q-gutter-md"
        >
            <q-input
            filled
            v-model="category.title"
            label="Enter a category"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
            />
            <div>
                <q-btn @click="validate" label="Add category" type="submit" color="primary"/>
                <q-btn @click="reset" label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
            </div>
        </q-form>

        </div>
        
        <q-list class="w-[400px] my-2" separator bordered>
            <q-item v-for=" category in categories.results " :key="category.id" v-ripple>
                <q-item-section>{{category.title}}</q-item-section>
                    <q-item-section class="p-0" avatar>
                        <q-icon @click="update(category.id,category)" class="transition cursor-pointer hover:scale-[120%]  text-amber-300" name="edit" />
                    </q-item-section>
                    <q-item-section avatar>
                        <q-icon @click="confirmDelete(category.id)" class="transition cursor-pointer hover:scale-[120%] text-red" name="close" />
                    </q-item-section>
            </q-item>
        </q-list>
        <q-btn v-if="next_page" color="primary" class="mb-2" icon-right="keyboard_double_arrow_down" label="load more" @click="loadmore()" />
    </div>
</template>


<script setup lang="ts">

import { useQuasar } from 'quasar';
import { addCategory,getCategories,deletCategory,updateCategory} from 'src/services/articles/api';
import { usePostsStore } from "src/stores/posts";
import { onBeforeMount,onUpdated, ref } from 'vue';

const $q = useQuasar()
const myForm = ref(null)
const next_page = ref<string|null>()

const category = ref<API.CategoryForm>( {
    title:null
})


const categories = ref<API.CategoryData>( {
        count:0,
        next:null,
        previous:'',
        results:[]

})



onBeforeMount(
    async () => {
        await getCategories(null).then((res)=>{
            categories.value.results = res.data.results
            next_page.value = res.data.next
        })
    },
    
)

function validate () {
    console.log('my form before');
    
    console.log(myForm.value);
    
    myForm.value.validate().then(success => {
        if (success) {
            addCategory(category.value).then((res)=>{
                categories.value = {
                    ...categories.value,
                    next: res.data.next,
                    previous: res.data.previous,
                    results: [
                        res.data,
                        ...categories.value.results,
                    ]
                }
            })
        }
        else {
        console.log('form not submited');
        
        }
    })

    }

// to reset validations:
function reset () {
    console.log(myForm);
    myForm.value.resetValidation()
    category.value = {
        title:null
    }
    console.log('form reset');
    
    }


function loadmore(){
        getCategories(next_page.value).then((res)=>{
            let current_content = categories.value.results
            const next_content = res.data.results

            next_page.value = res.data.next
            
            /* categories.value.results = res.data.results */
            current_content = [...current_content,...next_content]
            categories.value.results = current_content
            
            
        })

}

function confirmDelete (id:number) {
    $q.dialog({
        title: 'Confirm delete',
        message: 'Are you sure you want to delete this categorie!'
    }).onOk(() => {
        
        
        deletCategory(id).then((res)=>{
            console.log(id);
            console.log(categories.value.results)
            const newArr = categories.value.results.filter(object => {
            return object.id !== id;
            }); 
            categories.value.results = newArr
        })
    })
    
}

function update (id:number,category:API.CategoryForm) {
      $q.dialog({
        title: 'edit category',
        prompt: {
          model:category.title,
          type: 'text' 
        },
        cancel: true,
        persistent: true
      }).onOk(data => {
        const category = {
            title:data
        }
        
        updateCategory(id,category).then()
        const index = categories.value.results.findIndex((el) => el.id === id)
            categories.value.results[index] = {
                id:id,
                title: data,
            }
      })
    }



/* async function loadmore() {
    await getCategories(next_page).then((res)=>{
        next_page.value = res.data.next
        console.log(res.data.next);
    })
} */

</script>