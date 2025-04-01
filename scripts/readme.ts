import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

interface Category {
  id: string
  title: string
  sort: number
}

interface Guide {
  id: string
  title: string
  createdAt: string
  categories: string[]
}

const CATEGORIES_DIR = path.join(process.cwd(), 'data/categories')
const GUIDES_DIR = path.join(process.cwd(), 'data/guides')
const README_PATH = path.join(process.cwd(), 'README.md')

function getCategories(): Category[] {
  const files = fs.readdirSync(CATEGORIES_DIR)
  return files
    .map(file => {
      const content = fs.readFileSync(path.join(CATEGORIES_DIR, file), 'utf8')
      const { data } = matter(content)
      return {
        id: file.replace('.md', ''),
        title: data.title,
        sort: data.sort
      }
    })
    .sort((a, b) => a.sort - b.sort)
}

function getGuides(): Guide[] {
  const files = fs.readdirSync(GUIDES_DIR)
  return files
    .map(file => {
      const content = fs.readFileSync(path.join(GUIDES_DIR, file), 'utf8')
      const { data } = matter(content)
      return {
        id: file.replace('.md', ''),
        title: data.title,
        createdAt: data.createdAt,
        categories: data.categories || []
      }
    })
    .sort((a, b) => new Date(a.createdAt).getTime() - new Date(b.createdAt).getTime())
}

function generateMarkdownList() {
  const categories = getCategories()
  const guides = getGuides()
  
  let markdown = ''
  
  categories.forEach(category => {
    markdown += `* [${category.title}](https://bytebytego.com/guides/${category.id})\n`
    
    const categoryGuides = guides.filter(guide => guide.categories.includes(category.id))
    if (categoryGuides.length > 0) {
      categoryGuides.forEach(guide => {
        markdown += `  * [${guide.title}](https://bytebytego.com/guides/${guide.id})\n`
      })
    }
  })
  
  return markdown
}

function updateReadmeToc() {
  const readmeContent = fs.readFileSync(README_PATH, 'utf8')
  const tocRegex = /<!-- TOC -->\n([\s\S]*?)\n<!-- \/TOC -->/
  const newToc = `<!-- TOC -->\n\n${generateMarkdownList()}\n\n<!-- /TOC -->`
  const updatedContent = readmeContent.replace(tocRegex, newToc)
  fs.writeFileSync(README_PATH, updatedContent)
  console.log('TOC updated successfully!')
}

updateReadmeToc()
