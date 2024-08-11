<template>
    <Heder/>
    
    <Splitter style="height: 100%" class="mb-8">
        <SplitterPanel class="flex items-center justify-center" :size="15" :minSize="15">
            <Tree :value="tree" :filter="true"  filterMode="lenient" selectionMode="single"  class="w-full md:w-[30rem]" @nodeSelect="onNodeSelect"></Tree>
        </SplitterPanel>
        <SplitterPanel class="flex items-center justify-center"  :size="85" >
            <ScrollPanel style="width: 100%; height: 100%">
                <Accordion value="0" v-if="selected_node&&selected_node.data">
                    <AccordionPanel v-for="(event, index) in selected_node.data.log" :key="index" :value="index" multiple>
                        <AccordionHeader>{{ event.heder }}</AccordionHeader>
                        <AccordionContent>
                            <Tree :value="jsonToTreeNodes_(event)"  class="w-full md:w-[30rem]"></Tree>
                        </AccordionContent>
                    </AccordionPanel>
                </Accordion>
                <p v-else></p>
            </ScrollPanel>
        </SplitterPanel>
    </Splitter>
 </template>
  
<script>
    import Heder from './Heder.vue';
    import Splitter from 'primevue/splitter';
    import SplitterPanel from 'primevue/splitterpanel';
    import axios from 'axios';
    import Tree from 'primevue/tree';
    import Accordion from 'primevue/accordion';
    import AccordionPanel from 'primevue/accordionpanel';
    import AccordionHeader from 'primevue/accordionheader';
    import AccordionContent from 'primevue/accordioncontent';
    import JSONItem from './JSONItem.vue';
    import ScrollPanel from 'primevue/scrollpanel';


    class TreeNode {
    constructor(name, type, path, children = [],data = null) {
            this.label = name;
            this.type = type;
            this.path = path;
            this.data = data;
            this.children = children;
            // this.children = children.map(child => new TreeNode(child.name, child.type));
        }
    }

    function jsonToTreeNodes(jsonData, path = "") {
       return jsonData.map(item => new TreeNode(item.name, item.type, path+"/"+item.name, item.children ? jsonToTreeNodes(item.children, path+"/"+item.name) : []));
    }


    export default {
        components:{
            Heder,
            Splitter,
            SplitterPanel,
            Tree,
            Accordion,
            AccordionPanel,
            AccordionHeader,
            AccordionContent,
            JSONItem,
            ScrollPanel,
        },

        data() {
        return {
                tree:null,
                selected_node:null,
            }
        },

        created(){
            let context = this;
            axios.get(import.meta.env.VITE_BASE_ADRR+import.meta.env.VITE_GET_LOGS_TREE,)
            .then(function (response) {
                console.log(response);
                context.tree = jsonToTreeNodes(response.data);
                // context.tree = 
            })
            .catch(function (error) {
                console.log(error);
            });
        },

        methods: {
            onNodeSelect(event) {
                this.selected_node = event;

                axios.get(import.meta.env.VITE_BASE_ADRR+import.meta.env.VITE_GET_LOG+"?path="+encodeURIComponent(event.path))
                .then(function (response) {
                    console.log(response.data);
                    event.data = response.data;
                })
                .catch(function (error) {
                    console.log(error);
                });
            },

            jsonToTreeNodes_(jsonData, path = "") {
                let context = this;
                if (Array.isArray(jsonData)){
                    console.log(jsonData)
                    let res = [];
                    jsonData.forEach((value, key)  => 
                        {
                            res.push(new TreeNode(key+": "+(Array.isArray(value)|| (typeof (value) === 'object'&&value!=null) ? "":value)
                            , null, null, 
                            Array.isArray(value)|| typeof (value) === 'object' ? context.jsonToTreeNodes_(value) : [], 
                            Array.isArray(value)|| typeof (value) === 'object' ? null:value))
                        }
                    );
                    console.log(res);
                    return res;
                }
                else{
                    console.log(jsonData)
                    let res = [];
                    Object.entries(jsonData).forEach(([key, value])  => {
                        res.push( new TreeNode(key+": "+(Array.isArray(value)|| (typeof (value) === 'object'&&value!=null) ? "":value)
                        , null, null, 
                        Array.isArray(value)|| (typeof (value) === 'object'&&value!=null) ? context.jsonToTreeNodes_(value) : [],
                        Array.isArray(value)|| (typeof (value) === 'object'&&value!=null) === 'object' ? null:value))
                    });
                    console.log(res);
                    return res;
                }
            }
        },
    }
</script>
