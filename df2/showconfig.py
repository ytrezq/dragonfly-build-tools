import sys
import json

def showconfig(args):
	json.dump(args.config, sys.stdout, indent=1)

def showformat(args):
	print """
{
	"po2js": {
		/**
		  * Used by 'df2 po2js'. JS file will only be created for the languages
		  * defined here. The default list is:
		  */
		"langs": ["be", "bg", "cs", "da", "de", "el", "en-GB", "es-ES", "es-LA", 
		          "et", "fi", "fr", "fr-CA", "fy", "gd", "hi", "hr", "hu", "id",
		          "it", "ja", "ka", "ko", "lt", "mk", "nb", "nl", "nn", "pl",
		          "pt", "pt-BR", "ro", "ru", "sk", "sr", "sv", "ta", "te", "tr",
		          "uk", "vi", "zh-cn", "zh-tw"]
	},
	"build": {
		/**
		  * Default build values.
		  */
		"default_profile": {
			/**
			  * The name of a profile. Used with 'df2 build <name>'.
			  */
			"name": "",
			/**
			  * The source path for the build.
			  */
			"src": "src",
			/**
			  * The destination path of the build.
			  */
			"dest": "build",
			/**
			  * A list of source repositories which should not be copied 
			  * to the destination.
			  */
			"copy_blacklist": ["scripts",
			                   "ui-style",
			                   "ecma-debugger", 
			                   "ui-strings",
			                   "ui-scripts",
			                   "lib",
			                   "resource-manager",
			                   "syntaxhighlight"],
			/**
			  * Setting to specify if all JS files in the source repository
			  * should be checked to have an UTF-8 BOM.
			  */
			"verify_bom": true,
			/**
			  * Setting to specify if image resources should be converted 
			  * to data URIs.
			  */
			"make_data_uris": true,
			/**
			  * Setting to specify if the license should be included e in the 
			  * destination files.
			  */
			"license": true,
			/**
			  * Setting to specify if the destination can be overwritten.
			  */
			"force_overwrite": true,
			/**
			  * The destination path for the build log.
			  */
			"logs": "",
			/**
			  * Setting to specify if a build log should be created.
			  */
			"create_log": false,
			/**
			  * The destination path for the zipped builds.
			  */
			"zips": "",
			/**
			  * Setting to specify if a build should be zipped.
			  */
			"create_zips": false,
			/**
			  * Setting to specify if a build should be translated.
			  */
			"translate": false,
			/**
			  * Setting to specify if the JS files in destination should
			  * be minified.
			  */
			"minify": false,
			/**
			  * A list of paths which should not be minified.
			  */
			"minify_blacklist": [],
			/**
			  * Setting to specify if application cache manifests should
			  * be created.
			  */
			"create_manifests": false,
			/**
			  * The repository name which represents the server root.
			  */
			"manifest_root": "",
			/**
			  * The repository name which represents the server root.
			  * If set a base tag will be added to the XML files. The href
			  * attribute will be set to the difference of the actual location
			  * of the file to the specified value. This is to handle rewrites 
			  * on the server.
			  */
			"base_root_dir": ""
		},
		"profiles": {
			/**
			  * The default profile. Will be used if 'df2 build' is used without
			  * arguments.
			  */
			"default": {},
			/**
			  * Any number of profiles. Only non-default values need to be specified.
			  */
			"some_profile": {}
		}
	}
}
"""

def setup_subparser(subparsers, config):
	subp = subparsers.add_parser('showconfig', help="Show the config file.")
	subp.set_defaults(func=showconfig)
	subp = subparsers.add_parser('configformat', help="Show the config options.")
	subp.set_defaults(func=showformat)
	