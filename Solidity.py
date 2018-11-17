import sublime
import sublime_plugin


class NewSolidityCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		solidityBody = '''pragma solidity ^0.4.24;
		
/**
 * @title 
 * @dev
 * @author
 */
contract contractName{

	constructor() public{

	}
}
'''
		newView = self.view.window().new_file()
		newView.insert(edit,0,solidityBody)
