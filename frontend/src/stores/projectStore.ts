import { defineStore } from 'pinia'

export const useProject = defineStore('project', {
    state: () => ({
        showInfo: false,
        infoData: null as string | null,
        projectName: null as string | null,
        showVideo: false,
        VideoUrl: null as null | string
    })  
})