#include "FiberfrogApp.h"
#include "Moose.h"
#include "AppFactory.h"
#include "ModulesApp.h"
#include "MooseSyntax.h"

template<>
InputParameters validParams<FiberfrogApp>()
{
  InputParameters params = validParams<MooseApp>();
  return params;
}

FiberfrogApp::FiberfrogApp(InputParameters parameters) :
    MooseApp(parameters)
{
  Moose::registerObjects(_factory);
  ModulesApp::registerObjects(_factory);
  FiberfrogApp::registerObjects(_factory);

  Moose::associateSyntax(_syntax, _action_factory);
  ModulesApp::associateSyntax(_syntax, _action_factory);
  FiberfrogApp::associateSyntax(_syntax, _action_factory);
}

FiberfrogApp::~FiberfrogApp()
{
}

// External entry point for dynamic application loading
extern "C" void FiberfrogApp__registerApps() { FiberfrogApp::registerApps(); }
void
FiberfrogApp::registerApps()
{
  registerApp(FiberfrogApp);
}

// External entry point for dynamic object registration
extern "C" void FiberfrogApp__registerObjects(Factory & factory) { FiberfrogApp::registerObjects(factory); }
void
FiberfrogApp::registerObjects(Factory & factory)
{
}

// External entry point for dynamic syntax association
extern "C" void FiberfrogApp__associateSyntax(Syntax & syntax, ActionFactory & action_factory) { FiberfrogApp::associateSyntax(syntax, action_factory); }
void
FiberfrogApp::associateSyntax(Syntax & /*syntax*/, ActionFactory & /*action_factory*/)
{
}
