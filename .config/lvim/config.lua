-- Read the docs: https://www.lunarvim.org/docs/configuration
-- Example configs: https://github.com/LunarVim/starter.lvim
-- Video Tutorials: https://www.youtube.com/watch?v=sFA9kX-Ud_c&list=PLhoH5vyxr6QqGu0i7tt_XoVK9v-KvZ3m6
-- Forum: https://www.reddit.com/r/lunarvim/
-- Discord: https://discord.com/invite/Xb9B4Ny
 local opt = vim.opt
--opt.termguicolors = true



lvim.transparent_window = true


lvim.colorscheme = "pywal"
local pywal = require('pywal')

pywal.setup()
lvim.plugins = {
  {"karb94/neoscroll.nvim"},
  {"AlphaTechnolog/pywal.nvim"},
  {"norcalli/nvim-colorizer.lua"}
}

require('neoscroll').setup({
  mapping={},
  hide_cursor = true,          -- Hide cursor while scrolling
  stop_eof = true,             -- Stop at <EOF> when scrolling downwards
  respect_scrolloff = false,   -- Stop scrolling when the cursor reaches the scrolloff margin of the file
  cursor_scrolls_alone = true,
  easing = 'linear',           -- Default easing function
  pre_hook = nil,              -- Function to run before the scrolling animation starts
  post_hook = nil,             -- Function to run after the scrolling animation ends
  performance_mode = false,

})

--[[  I WAS TRYING SOMETING HERE BUT DIDNT WORK 
local colorschemes ={['pywal']='AlphaTechnolog/pywal.nvim'}
local selectedColorscheme = 'pywal'
return {
	colorschemes[selectedColorscheme],
	lazy = false,
	priority = 1000,
	config = function()
		-- load colorscheme here
		local cmd = 'colorscheme ' .. selectedColorscheme
		vim.cmd(cmd)
	end,
}
]]--
